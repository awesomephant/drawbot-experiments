from drawbot_skia.drawbot import *
from util.mark import mark
from util.coin import coin

# from util.grid import draw_grid
import random
import datetime
import math
from hsluv import *

output_path = "./output/gradients/"
ts = str(datetime.datetime.now().timestamp())
markPoints = False

canvas_width = 2000
canvas_height = 1500
margin = 50


def draw_grid(x_0, y_0, w, h, interval=50, r=5):
    cols = math.floor(w / interval) + 1
    rows = math.floor(h / interval) + 1

    for i in range(cols * rows):
        x = x_0 + (i % cols) * interval
        y = y_0 + math.floor(i / cols) * interval
        oval(x - r / 2, y - r / 2, r, r)
        thickness = 0.2
        # rect(x - r / 2, y - r * thickness / 2, r, r * thickness)
        # rect(x - r * thickness / 2, y - r / 2, r * thickness, r)


def draw_gradient(x_0, y, h, ratio):
    steps = 40
    x = x_0
    hue = 250
    saturation = 100
    value = 0
    w = 3.85
    for i in range(steps):
        w = w * ratio
        hue += ratio * i * 0.03
        saturation = saturation + ratio * 2
        value = value + ratio * 2

        color = hsluv_to_rgb([hue, saturation, value])
        # fill(*color)
        stroke(1,1,1)
        rect(x, y, w, h)
        x += w


def draw():
    draw_gradient(margin, margin, 1400, 1.1)
    fill(0, 0, 0, 0.2)
    # draw_grid(0, 0, canvas_width, canvas_height)
    # draw_gradient(margin, margin + 420, 200, 1.2)


size(canvas_width, canvas_height)
# fill(0.6, 0.6, 0.6, 1)
fill(0, 0, 0, 1)
rect(0, 0, canvas_width, canvas_height)

draw()
saveImage(output_path + "test-gradient" + ".png")
# saveImage(output_path + ts + ".png")
