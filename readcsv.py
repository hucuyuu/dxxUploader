import csv


def get_name(id):
    with open("1904.csv") as f:
        csv_reader = csv.reader(f)
        for i in csv_reader:
            if i[0] == id:
                return i[0], i[1]
    return ()
