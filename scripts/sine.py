from drawbot_skia.drawbot import *
from util.mark import mark
from util.coin import coin

# from util.grid import draw_grid
import random
import datetime
import math
from hsluv import *

output_path = "./output/"
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


def draw_sine(x_0, y_0):
    steps = 400
    scale_y = 100
    scale_x = 5
    path = BezierPath()
    path.moveTo((x_0, y_0))

    for i in range(steps):
        y = math.sin(i * .1 - math.pi * .5) + 1
        y_scaled = y_0 + y * scale_y
        x_scaled = x_0 + i * scale_x
        path.lineTo((x_scaled, y_scaled))

    drawPath(path)


def draw():
    stroke(0,0,0,1)
    draw_sine(margin, margin)


size(canvas_width, canvas_height)
fill(.5, .5, .5, 1)
rect(0, 0, canvas_width, canvas_height)
draw()
saveImage(output_path + "test-sine" + ".png")

# saveImage(output_path + ts + ".png")
