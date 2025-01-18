from drawbot_skia.drawbot import *
from util.mark import mark
from util.coin import coin
import random
import datetime
import math
from hsluv import *

output_path = '../output/'
ts = str(datetime.datetime.now().timestamp())
markPoints = True
w = 2500
h = 2500

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


margin = 50

red = (.5, .38, 0.1216)
yellow = (1, .8314, 0)
green = (.1, 0.250, .1647)
blue = (.3, .5, .9)
orange = (1, .4588, 0)
white = (1, 1, 1)
colors = [red, green, blue]


def draw():
    # count = random.randrange(50,100)
    ring_count = 10
    center = (w / 2, h / 2)
    dot_radius = 60

    for r in range(ring_count):
        dot_count = r * 6
        angle_offset = 3
        c = r * 2 * dot_radius * .99
        fill(0, 0, 0, 0)
        stroke(1, 1, 1, 1)
        stroke(0, 0, 0, 1)
        oval(center[0] - c, center[1] - c, c * 2, c * 2)
        for i in range(dot_count):
            
            # color = hsluv_to_rgb([2 * i + 80, 90, 60])

            color = random.choice(colors)
            angle = (((360 / dot_count) * i) +
                     (angle_offset * r)) * (math.pi/180)
            adjacent = c * math.cos(angle)
            opposite = c * math.sin(angle)

            x = center[0] + adjacent - dot_radius
            y = center[1] + opposite - dot_radius

            stroke(1, 1, 1, 0)
            # fill(.008, .2588 * .2 * r, 1 - r * .2 * i)
            fill(*color)
            if (coin(.65)):
                rad = (dot_radius * 2) - r * 4
                oval(x, y, rad, rad)
                fill(0,0,0)
                # mark((x + rad / 2,y + rad / 2))


size(w, h)
fill(0.75, 0.74, 0.73, 1)
rect(0, 0, w, h)

draw()

# saveImage(output_path + ts + ".png")
saveImage(output_path + "flower.png")
