from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
from wand.color import Color
import os


def draw_id(stu, filename):
    with open('upload/%s' % filename, 'rb') as f:
        image_binary = f.read()

    with Image(blob=image_binary) as img:
        with Drawing() as draw:
            draw.font = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
            draw.font_size = 150
            draw.fill_color = Color('#00F5FF')
            draw.gravity = 'center'
            draw.text(0, 0, '%s\n%s' % (stu[1], stu[0]))
            draw(img)
            img.format = 'jpeg'
            # img.save(filename='text.png')
            with open('modified/%s' % filename, 'wb') as to_save:
                to_save.write(img.make_blob())
