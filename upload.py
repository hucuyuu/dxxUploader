# system lib
from flask import Flask, render_template, request, redirect, abort, send_from_directory
from werkzeug.utils import secure_filename
import os

# user  lib
import readcsv
import writecsv
import autops
import requests

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload'
mainServerUrl = 'website'


@app.route('/modified/<imgFile>', methods=['GET'])
# show modified img
def showModifiefImage(imgFile):
    if len(secure_filename(imgFile)) != 0:
        directory = os.path.join(os.getcwd(), 'modified')
        return send_from_directory(directory, secure_filename(imgFile), as_attachment=True)
    else:
        return "Opps something should not happen happened!"


@app.route('/upload/<number>')
# upload here
def upload_file(number):
    if number.isdigit():
        dxxNumber = number
    else:
        abort(404)
    dxxNumber2 = int(dxxNumber)
    if dxxNumber2 < 21 and dxxNumber2 >= 0:
        return render_template('upload.html', dxxNumber=dxxNumber, serverUrl=mainServerUrl)
    else:
        abort(404)


@app.route('/count/<number>')
# count upload
def count_upload(number):
    if number.isdigit():
        dxxNumber = number
        sum = writecsv.count_value(dxxNumber)
        return str(sum)
    else:
        abort(404)


@app.route('/uploader', methods=['GET', 'POST'])
# post processor
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        studentId = request.form.get('studentId')
        dxxNumberPost = request.form.get('dxxNumberPost')
        filePrefix = dxxNumberPost + '_' + studentId + '__'
        stu = readcsv.get_name(studentId)
        if stu and len(secure_filename(f.filename)) != 0:
            dxxImgUrl = filePrefix + secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'],
                                filePrefix +
                                secure_filename(f.filename)
                                ))
            autops.draw_id(stu, dxxImgUrl)
            writecsv.write_true(studentId, dxxNumberPost)
            # return render_template('uploadOK.html', dxxNumberPost=dxxNumberPost, dxxImgUrl=dxxImgUrl, serverUrl=imgServerUrl)
            return render_template('uploadOK.html', dxxNumberPost=dxxNumberPost, dxxImgUrl=dxxImgUrl)
        elif len(secure_filename(f.filename)) == 0:
            return render_template('uploadEmpty.html', dxxNumberPost=dxxNumberPost)
        elif not stu:
            return render_template('uploadBadID.html', dxxNumberPost=dxxNumberPost, studentIdPost=studentId)
        else:
            return "Opps something should not happen happened!"


@app.route('/p')
# show pi-dashoboard
def index():
    return redirect("http://website")
    # return requests.get("http://website").text


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=5000,
            debug=True)
