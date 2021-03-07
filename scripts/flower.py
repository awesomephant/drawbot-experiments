from drawbot_skia.drawbot import *
from util.mark import mark
from util.coin import coin
import random
import datetime
import math

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

red = (1, .1804, 0.1216)
yellow = (1, .8314, 0)
green = (.066, 0.850, .1647)
blue = (.008, .2588, 1)
orange = (1, .4588, 0)
white = (1, 1, 1)
colors = [yellow]


def draw():
    # count = random.randrange(50,100)
    ring_count = 18
    center = (w / 2, h / 2)
    dot_radius = 20

    for r in range(ring_count):
        dot_count = r * 6
        angle_offset = 3
        c = r * 2 * dot_radius * 1
        fill(0, 0, 0, 0)
        stroke(1, 1, 1, 1)
        # stroke(0, 0, 0, 1)
        oval(center[0] - c, center[1] - c, c * 2, c * 2)
        for i in range(dot_count):
            color = random.choice(colors)
            angle = (((360 / dot_count) * i) +
                     (angle_offset * r)) * (math.pi/180)
            print(angle)
            adjacent = c * math.cos(angle)
            opposite = c * math.sin(angle)

            x = center[0] + adjacent - dot_radius
            y = center[1] + opposite - dot_radius

            stroke(1, 1, 1, 0)
            fill(*color)
            if (coin(.8)):
                oval(x, y, dot_radius * 2, dot_radius * 2)

    line_count = 50


size(w, h)
fill(0.75, 0.74, 0.73, 1)
rect(0, 0, w, h)

draw()

saveImage(output_path + ts + ".png")
