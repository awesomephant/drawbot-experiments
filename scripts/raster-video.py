from contextlib import closing
from drawbot_skia.drawbot import *
import random
import datetime
import math
import time
from PIL import Image

output_path = '../output/'
input_path = '../input/'

glyphs = list("bcdf jABCDEEFIKLYXZ")
random.shuffle(glyphs)
w = 1200
h = 1200
size(w, h)

def value_to_glyph(v):
    interval = 1 / len(glyphs)
    return glyphs[math.floor(v/interval) - 1]

def draw_image(input, output, target_size):
    newDrawing()
    t_start = time.perf_counter()
    input_image = Image.open(input_path + input)
    image = input_image.rotate(180)
    image.thumbnail((target_size, target_size), Image.ANTIALIAS)

    imageWidth = image.width
    imageHeight = image.height

    scaleY = h / imageHeight
    scaleX = scaleY
    padding = 2
    font("Ornaments", scaleX - padding)
    fill(0, 0, 0, 1)
    rect(0, 0, w, h)
    fill(1, 1, 1, 1)


    for i, pixel in enumerate(image.getdata(), 0):
        x = i % imageWidth
        y = math.floor(i / imageWidth)

        if type(pixel) is tuple:
            value = (sum(pixel) / 4) / 255
        else:
            value = pixel / 255

        text(value_to_glyph(value), (x * scaleX, y * scaleY))

    saveImage(output_path + output)
    
    input_image.close()
    image.close()
    
    t_end = time.perf_counter()
    print("Wrote " + output_path + output + " (" + str(t_end - t_start) + "s)")



scale = 60
for i in range(453, 1453):
    if (i % 100 == 0):
        scale = random.randrange(40, 150)
        random.shuffle(glyphs)

    draw_image("frames/frame" + str(i) + ".png",
               "video/" + str(i) + ".png",  scale)
