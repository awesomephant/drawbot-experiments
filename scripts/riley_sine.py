from drawbot_skia.drawbot import *
from util.mark import mark
import random
import datetime
import math
from util.grid_lines import draw_grid

output_path = '../output/riley/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())
markPoints = False
w = 1500
h = 1200


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

margin = 50

def wave(p0, p1, amplitude, frequency, phase=0, width=20, point_count=50):
    points = []
    for n in range(point_count + 1):
        x = p0[0] + ((p1[0] - p0[0]) / point_count) * n
        y = amplitude * math.sin(2 * math.pi * frequency * x + phase)
        y += p0[1]
        points.append((x, y))

    path = BezierPath()
    path.moveTo(points[0])
    for p in points:
        path.lineTo(p)
    
    path.lineTo((points[-1][0],points[-1][1] + width))
    for p in reversed(points):
        path.lineTo((p[0], p[1] + width))
    path.closePath()
    drawPath(path)


def draw(frame):
    line_count = 24
    blendMode('multiply')
    fill(.9, .9, .9, 1)
    rect(0, 0, w, h)
   
    # fill(0, 0, 0, 0)
    stroke(.7,.7,.7,1)
    fill(.8, .8, .8, 0)
    strokeWidth(1)
    draw_grid(margin, margin, w - margin * 2, h - margin * 2, 10, line_count)
    # resolution = math.floor(5 + math.sin(frame * .1) * 50)

    for i in range(line_count):
        a = 35
        y = ((h - margin * 2.5) / line_count) * i + margin * 1.5
        phase = 5 * math.sin(.035 * i + frame * .01)
        width = (1 + math.sin((i + frame * .5) * .2)) * 17 + 1
        resolution = 30
        stroke(0,0,0,0)
        fill(.95, .3, .0, 1)
        wave((margin, y), (w - margin, y), a, .0025, phase, width, resolution)


frame_count = 240

for i in range(frame_count):
    newDrawing()
    size(w, h)
    print("Frame ", i, "/", frame_count)
    draw(i)
    saveImage(output_path + "/frame_" + str(i) + ".png")