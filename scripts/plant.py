from drawbot_skia.drawbot import *
from opensimplex import OpenSimplex
import random
import datetime
import math

noise = OpenSimplex()

output_path = '../output/plant/'
input_path = '../input/'
ts = str(datetime.datetime.now().timestamp())
markPoints = False
w = 1000
h = 1000


def mark(x, y, r=8):
    if markPoints:
        rect(x - r / 2, y - r / 2, r, r)
    return


def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def profile(x, noiseSeed=0):
    # We're going to assume x is between 0 and 1
    randomValue = noise.noise2d(x * 6, noiseSeed) * .2 + 1
    y = math.sin(math.pi * x) * randomValue
    return y


def line(p1, p2):
    fill(0, 0, 0, 0)
    stroke(0, 0, 0, 1)
    path = BezierPath()
    path.moveTo(p1)
    path.lineTo(p2)
    drawPath(path)


def leaf(start, end, n_points=100):
    stroke(0, 0, 0, 1)
    d = math.sqrt(((end[0] - start[0])**2) + ((end[1] - start[1]) ** 2))
    direction = ((end[0] - start[0]) / d, (end[1] - start[1]) / d)
    perpendicular = (direction[1], direction[0] * -1)  # Note we transpose
    spine_points = []
    outline = []

    print("Leaf direction: " + str(direction))
    print("Perpendicular: " + str(perpendicular))
    print("Spine length: " + str(d))

    # We generate points on the spine
    ns = random.randrange(0, 1000)
    for n in range(n_points):
        randomValue = noise.noise2d(n * .2, ns)
        offset = (perpendicular[0] * randomValue,
                  perpendicular[1] * randomValue)
        point = (start[0] + direction[0] * (d / n_points) * n + offset[0],
                 start[1] + direction[1] * (d / n_points) * n + offset[1])
        spine_points.append(point)

    # Then we make the outline of the leaf
    # The first half...
    ns = random.randrange(0, 1000)
    length_scale = d / 5
    for i, p in enumerate(spine_points):
        x = (i / (n_points - 1))
        length = profile(x, ns) * length_scale
        outer_point = (p[0] + perpendicular[0] * length,
                       p[1] + perpendicular[1] * length)
        outline.append(outer_point)

    # and the second half, going backward
    ns = random.randrange(0, 1000)
    for i, p in reversed(list(enumerate(spine_points))):
        x = (i / (n_points - 1))
        length = profile(x, ns) * length_scale
        outer_point = (p[0] - perpendicular[0] * length,
                       p[1] - perpendicular[1] * length)
        outline.append(outer_point)

    # Let's draw the spine of the leaf first
    spine = BezierPath()
    spine.moveTo(start)
    for p in spine_points:
        # mark(p[0], p[1])
        spine.lineTo(p)
    drawPath(spine)
    spine.endPath()

    # Then we draw the profiles
    fill(0, .0, .0, 1)
    path = BezierPath()
    path.moveTo(start)
    for p in outline:
        path.lineTo(p)
        mark(p[0], p[1])
    path.closePath()
    drawPath(path)


def branch(start):
    # Let's generate the points of the branch
    points = [(start[0], start[1])]
    ns = random.randrange(0, 1000)
    pointCount = 20
    for i in range(pointCount):
        randomValue = (noise.noise2d(i * .5, ns) * 40)
        p = (points[i][0] + randomValue, points[i]
             [1] + ((h - 150) / pointCount))
        points.append(p)

    stroke(0, 0, 0, 1)
    path = BezierPath()
    path.moveTo(start)

    for i, p in enumerate(points):
        if i > len(points) - 2:
            break
        mark(p[0], p[1])
        path.lineTo(p)
        np = points[i+1]
        segment_length = math.sqrt(((np[0] - p[0])**2) + ((np[1] - p[1]) ** 2))
        segment_direction = (
            (np[0] - p[0]) / segment_length, (np[1] - p[1]) / segment_length)
        segment_perpendicular = (
            segment_direction[1], -1 * segment_direction[0])
        length = 100
        #line(p, (p[0] + segment_perpendicular[0] * 10,p[1] + segment_perpendicular[1] * 10))
        if (isEven(i)):
            leaf(p, (p[0] + segment_perpendicular[0] * length,
                     p[1] + 100 + segment_perpendicular[1] * length), 80)
        else:
            leaf(p, (p[0] - segment_perpendicular[0] * length,
                     p[1] + 100 + segment_perpendicular[1] * length), 80)
    fill(0, .0, .0, 0)
    drawPath(path)


def draw():
    branch((510, 25))


size(w, h)
fill(1, 1, 1, 1)
rect(0, 0, w, h)
fill(1, 1, 1, 0)
draw()
saveImage(output_path + "test3" + ".png")
