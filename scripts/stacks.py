from drawbot_skia.drawbot import *
from util.mark import mark
from util.coin import coin
import random
import datetime
import math
from hsluv import *

output_path = '../output/'
ts = str(datetime.datetime.now().timestamp())
markPoints = False
w = 1500
h = 1500


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


margin = 50


blue = 260
red = 14
green = 125

hues = [blue, red]


def draw_stack(x, y, height, radius=350, element_count=20):
    hue = random.choice(hues)
    for i in range(element_count):
        #value = (50 / element_count) * i + 50
        value = (40 / element_count) * i + 50
        saturation = 100 - (10 / element_count) * i
        color = hsluv_to_rgb([hue, saturation, value])
        fill(*color)
        #y_i = y + (height / element_count) * i
        #x_i = x

        x_i = x + random.randrange(-9, 10)
        y_i = y + random.randrange(-9, 10)
        x = x_i
        y = y_i
        oval(x_i, y_i, radius, radius * 1)


def draw():
    stack_count = 30
    for i in range(stack_count):
        r = random.randrange(70, 80)
        x = random.randrange(margin, w - margin - r)
        y = margin
        h = random.randrange(400, 1200)
        draw_stack(w / 2, h / 2, h, r, 4000)


size(w, h)
fill(0.75, 0.74, 0.73, 1)
rect(0, 0, w, h)

draw()

saveImage(output_path + ts + ".png")
