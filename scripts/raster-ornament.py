from drawbot_skia.drawbot import *
import random
import datetime
import math
from PIL import Image

output_path = '../output/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())

w = 1400
h = 1700

size(w, h)
fill(0, 0, 0, 1)
rect(0, 0, w, h)
fill(1, 1, 1, 1)

glyphs = list("TUVWXYZ   ")
random.shuffle(glyphs)

def value_to_glyph(v):
    interval = 1 / len(glyphs)
    return glyphs[math.floor(v/interval) - 1]


def draw_image(input, target_size):
    input_image = Image.open(input_path + input)
    image = input_image.rotate(180)
    image.thumbnail((target_size, target_size), Image.ANTIALIAS)
    image.rotate(180)

    imageWidth = image.width
    imageHeight = image.height

    scaleY = h / imageHeight
    scaleX = scaleY
    font("Ornaments", scaleX)

    for i, pixel in enumerate(image.getdata(), 0):
        x = i % imageWidth
        y = math.floor(i / imageWidth)
        if type(pixel) is tuple:
            value = (sum(pixel) / 4) / 255
        else:
            value = pixel / 255

        text(value_to_glyph(value), (x * scaleX, y * scaleY))


draw_image("Capture.PNG", 60)
# draw_image("dom-hill-nimElTcTNyY-unsplash.jpg", 60)
saveImage(output_path + ts + ".png")
