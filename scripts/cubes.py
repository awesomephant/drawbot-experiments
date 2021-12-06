from drawbot_skia.drawbot import *
import datetime
import random
import numpy as np
import math

from numpy.lib.shape_base import column_stack
from numpy.linalg.linalg import norm

output_path = "./output/cube/"
input_path = "../input/"
ts = str(datetime.datetime.now().timestamp())
canvas_width = 3100
canvas_height = 2700
z = 1000
draw_points = True
draw_verts = True
draw_faces = True

# o = np.array([random.randint(0, w), random.randint(0, 200), 0])
o = np.array([canvas_width / 2, random.randint(0, canvas_height), 0])
objects = []


def pointToString(p):
    return "[" + str(p[0]) + "," + str(p[1]) + "," + str(p[2]) + "]"


class ProjectedObject:
    def __init__(self, points, verts, faces, normals, fill):
        self.points = points
        self.verts = verts
        self.faces = faces
        self.normals = normals
        self.fill = fill


class ProjectedPoint:
    def __init__(self, p, visible):
        self.p = p
        self.visible = visible

class Cube:
    """
    Produces a basic representation of a cube.
    """

    def __init__(self, x, y, z, w, h, d):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        #self.fill = (1, 1, 1, 1)
        self.fill = (random.uniform(.8, .99), random.uniform(.7, .99), random.uniform(.2, .99), 0.98)

        # Let's write down the 8 points of the cube
        # front to back, starting bottom left (origin), clockwise
        self.points = [
            [x, y, z],
            [x, y + h, z],
            [x + w, y + h, z],
            [x + w, y, z],
            [x, y, z + d],
            [x, y + h, z + d],
            [x + w, y + h, z + d],
            [x + w, y, z + d],
        ]
        # Verts are connections between points,
        # so we'll just reference them by index
        self.verts = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],
            [0, 4],
            [1, 5],
            [3, 7],
            [2, 6],
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 4],
        ]
        # Faces are connections between points too,
        # so we'll reference them by index too
        self.faces = [
            [4, 5, 6, 7],
            [6, 2, 3, 7],
            [1, 2, 6, 5],
            [0, 4, 7, 3],
            [0, 1, 5, 4],
            [3, 2, 1, 0],
        ]
        self.normals = []


def arrow(p0, p1):
    r = 10
    line(p0, p1)
    oval(p1[0] - r / 2, p1[1] - r / 2, r, r)


def rotate(obj, u=(0, 0, 1), degrees=10):
    theta = degrees * math.pi / 180
    _points = []
    # First we need to work out the rotation matrix
    # The rotation axis is u
    # print("Rotating by ", degrees)
    r = np.array(
        [
            [
                math.cos(theta) + u[0] ** 2 * (1 - math.cos(theta)),
                u[0] * u[1] * (1 - math.cos(theta)) - u[2] * math.sin(theta),
                u[0] * u[2] * (1 - math.cos(theta)) + u[1] * math.sin(theta),
            ],
            [
                u[1] * u[0] * (1 - math.cos(theta)) + u[2] * math.sin(theta),
                math.cos(theta) + u[1] ** 2 * (1 - math.cos(theta)),
                u[1] * u[2] * (1 - math.cos(theta)) - u[0] * math.sin(theta),
            ],
            [
                u[2] * u[0] * (1 - math.cos(theta)) - u[1] * math.sin(theta),
                u[2] * u[1] * (1 - math.cos(theta)) + u[0] * math.sin(theta),
                math.cos(theta) + u[2] ** 2 * (1 - math.cos(theta)),
            ],
        ]
    )

    # Then we find the average position of the object points
    # (we'll pretend that's the center)
    center = np.sum(obj.points, axis=0) * 1 / len(obj.points)

    for p in obj.points:
        # Move the object to the origin
        point = np.array(p) - center

        # Do the rotation
        _p = np.matmul(r, point)

        # And move it back
        _p += center
        _points.append(_p)
        # print(points * r)
    obj.points = _points


def project(p):
    # Let's work out the projected point a' = (u,v,w)
    c = z / p[2]
    u = o[0] + c * (p[0] - o[0])
    v = o[1] + c * (p[1] - o[1])
    return [u, v, z]


def buildScene():
    for i in range(85):
        x = random.randint(-1000, 3000)
        y = random.randint(0, canvas_height + 3000)
        z = random.randint(500, 1500)
        w = random.randint(200, 800)
        h = random.randint(200, 800)
        d = random.randint(200, 800)
        c = Cube(x, y, z, w, h, d)
        objects.append(c)

def draw():
    newDrawing()
    size(canvas_width, canvas_height)
    # fill(0.9, 0.9, 0.91, 1)
    fill(1, 1, 1, 1)
    rect(0, 0, canvas_width, canvas_height)

    # First we throw some objects into the scene
    projectedObjects = []

    # Then we project all objects in the scene
    for obj in objects:
        projectedPoints = []
        projectedNormals = []
        culledFaces = []
        culledPoints = []
        for i, f in enumerate(obj.faces):
            # Perform backface culling, ie. drop all faces that
            # are pointing away from the viewer
            # We need an arbitrary vector on the face, so
            # let's just take the first two vertices
            a = np.array(obj.points[f[0]])
            b = np.array(obj.points[f[1]])
            c = np.array(obj.points[f[2]])

            ab = b - a
            ac = c - a
            oa = a - o
            oa = oa / np.linalg.norm(oa)
            n = np.cross(ab, ac) / np.linalg.norm(np.cross(ab, ac))
            # Let's add the normal to the object so we can draw it
            obj.normals.append([a, a + n * 200])

            angle = math.acos(np.dot(oa, n)) * 180 / math.pi
            # print("angle: " + str(angle))
            if not (angle >= 90):
                culledFaces.append(f)

        # Now we cull points that aren't connected to faces
        for i, p in enumerate(obj.points):
            visible = False
            for f in culledFaces:
                if i in f:
                    visible = True
            projectedPoints.append(ProjectedPoint(project(p), visible))

        for i, p in enumerate(culledPoints):
            projectedPoints.append(project(p))
        for i, n in enumerate(obj.normals):
            projectedNormals.append([project(n[0]), project(n[1])])

        projectedObjects.append(
            ProjectedObject(projectedPoints, obj.verts, culledFaces, projectedNormals, obj.fill)
        )

    # Then we draw our list of projected objects
    for i, obj in enumerate(projectedObjects):
        # print("Drawing " + str(i + 1) + "/" + str(len(projectedObjects)))
        fill(*obj.fill)
        for f in obj.faces:
            a = obj.points[f[0]].p
            b = obj.points[f[1]].p
            c = obj.points[f[2]].p
            d = obj.points[f[3]].p
            if draw_faces:
                polygon((a[0], a[1]), (b[0], b[1]), (c[0], c[1]), (d[0], d[1]))
        fill(0, 0, 0, 1)
        for v in obj.verts:
            # print("Drawing vert")
            stroke(0)            
            strokeWidth(2)            
            a = obj.points[v[0]]
            b = obj.points[v[1]]
            if a.visible and b.visible and draw_verts:
                line((a.p[0], a.p[1]), (b.p[0], b.p[1]))
        for n in obj.normals:
            a = n[0]
            b = n[1]
            # stroke(1, 0, 0)
            # fill(1, 0, 0)
            # arrow((a[0], a[1]), (b[0], b[1]))
        for i, p in enumerate(obj.points):
            point = p.p
            fill(0, 0, 0, 1)
            stroke(0, 0, 0, 0)
            if p.visible:
                # print("Drawing point")
                if draw_points:
                    oval(point[0] - 8, point[1] - 8, 16, 16)
                # text(str(i), (point[0] - 10, point[1]))


angle = -45
frame_count = 1
for i in range(frame_count):
    buildScene()
    print("Frame ", i, "/", frame_count)
    for obj in objects:
        rotate(obj, (.2, 1, -.2), angle)
    draw()
    saveImage(output_path + "/frames/frame_" + str(i) + ".png")
    objects = []


print("Done.")
# saveImage(output_path + str(ts)  + ".png")
# saveImage(output_path + "test" + ".svg")
