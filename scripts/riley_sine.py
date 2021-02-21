from drawbot_skia.drawbot import *
from util.mark import mark
import random
import datetime
import math

output_path = '../output/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())
markPoints = False
w = 1500
h = 1000


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

margin = 50

def wave(p0, p1, amplitude, frequency, phase=0, width=20, point_count=500):
    fill(1, 1, 1, 1)
    stroke(1, 1, 1, 0)
    points = []
    for n in range(point_count):
        x = ((p1[0] - p0[0]) / point_count) * n + margin
        y = amplitude * math.sin(2 * math.pi * frequency * x + phase)
        y += p0[1]
        points.append((x, y))

    path = BezierPath()
    path.moveTo(points[0])
    for p in points:
        #mark(p)
        path.lineTo(p)
    
    path.lineTo((points[-1][0],points[-1][1] + width))
    for p in reversed(points):
        path.lineTo((p[0], p[1] + width))
    path.closePath()
    drawPath(path)


def draw():
    line_count = 20
    for i in range(line_count):
        print("Drawing line " + str(i))
        a = 50
        phase = .1 * math.sin(2 * math.pi * .02 * i + 0)
        #phase = .002 * i
        y = ((h - margin * 2.5) / line_count) * i + margin * 1.5
        wave((margin, y), (w - margin, y), a, .003, phase * i, 30, 40)


size(w, h)
#fill(.99, .99, .99, 1)
fill(0, 0, 0, 1)
rect(0, 0, w, h)

draw()

saveImage(output_path + ts + ".png")
