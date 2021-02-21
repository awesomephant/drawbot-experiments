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


def wave(p0, p1, width, amplitude, waves, phase, c):
    fill(0, 0, 0, .1)
    stroke(0, 0, 0, 1)
    #
    points = []
    for w in range(waves + 1):
        x = (p1[0] - p0[0]) / ((waves + 1) / (w + 1))
        if isEven(w):
            y = p0[1]
            points.append((x, y))
        else:
            y = p0[1] + width
            points.append((x, y))

    path = BezierPath()
    path.moveTo(points[0])
    for n, p in enumerate(points[:-1]):
        print(p)
        p1 = points[n+1]
        path.curveTo((p[0] + c, p[1]), (p1[0] - c, p1[1]), p1)
        #mark(p[0], p[1])
        #text(str(n), (p[0] + 0, p[1] - 15))

    path.lineTo((points[-1][0], points[-1][1] + width))
    
    for n, p in enumerate(points):
        p = points[-n]
        p1 = points[- n - 1]
        y = p1[1] + width
        x = p1[0]
        if n > 0:
            path.curveTo((p[0] - c, p[1] + width), (x + c, y), (x, y))
            #mark(x, y)
            #text("B" + str(n), (x, y + 15))
    
    path.lineTo(points[0])
    drawPath(path)


def draw():
    line_count = 10
    margin = 10
    gap = 50
    for i in range(line_count):
        y = (h / line_count) * i 
        wave((margin, y), (w - margin, y), 60, 30, 16, 0, 70)


size(w, h)
fill(1, 1, 1, 1)
rect(0, 0, w, h)

draw()

saveImage(output_path + "test3" + ".png")
