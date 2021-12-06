from drawbot_skia.drawbot import *
from numpy.lib.shape_base import column_stack
from util.mark import mark
import datetime
import uuid
import numpy as np
import math

output_path = "./output/voronoi/"
ts = str(datetime.datetime.now().timestamp())
w = 800
h = 800
point_count = 20


class Triangle:
    def __init__(self, verts, neighbours):
        self.id = uuid.uuid4()
        self.verts = verts
        self.neighbours = neighbours


class Triangulation:
    def __init__(self, triangles):
        self.triangles = triangles

    def add_point():
        print("test")

def get_triangle_index(arr, search_id):
    for i, item in enumerate(arr):
        if item.id == search_id:
            return i
    print("Array element not found.")

    return False

def get_triangle_by_id(arr, search_id):
    for index, item in enumerate(arr):
        if item.id == search_id:
            return item
    print("Array element not found.")
    return False

def draw_triangles(_triangles):
    fill(0, 0, 1, 0)
    stroke(0,0,0,1)
    for t in _triangles:
        p = BezierPath()
        p.moveTo(t.verts[0])
        p.lineTo(t.verts[1])
        p.lineTo(t.verts[2])
        p.lineTo(t.verts[0])
        drawPath(p)


def draw_points(points):
    for i, v in enumerate(points):
        stroke(0, 0, 0, 1)
        mark(v)


def get_neighbour(dt, triangle, edge):
    for n in triangle.neighbours:
        neighbour = get_triangle_by_id(dt, n)
        matching_verts = 0
        for v in edge:
            for v_i in neighbour.verts:
                if np.array_equal(v, v_i):
                    matching_verts += 1
        if matching_verts == 2:
            return neighbour
    print("Couldn't find neighbour")
    return False


def get_orientation(a, b, p):
    m = np.array(
        [
            [a[0], a[1], 1],
            [b[0], b[1], 1],
            [p[0], p[1], 1],
        ]
    )

    o = np.linalg.det(m)
    return o

def update_neighbours(dt):
    for i, t in enumerate(dt):
        t.neighbours = []
        for j, t_j in enumerate(dt):
            if (i != j):
                matching_verts = 0
                for v in t.verts:
                    for v_j in t_j.verts:
                        if np.array_equal(v, v_j):
                            matching_verts += 1
                if matching_verts == 2:
                    t.neighbours = np.append(t.neighbours, t_j.id) 
    return dt

def get_opposite_edge(triangle, i):
    if i == 0:
        return [triangle.verts[2], triangle.verts[1]]
    if i == 1:
        return [triangle.verts[0], triangle.verts[2]]
    if i == 2:
        return [triangle.verts[1], triangle.verts[0]]


def is_in_circle(a, b, c, p):
    m = np.array(
        [
            [a[0], a[1], a[0] ** 2 + a[1] ** 2, 1],
            [b[0], b[1], b[0] ** 2 + b[1] ** 2, 1],
            [c[0], c[1], c[0] ** 2 + c[1] ** 2, 1],
            [p[0], p[1], p[0] ** 2 + p[1] ** 2, 1],
        ]
    )
    o = np.linalg.det(m)
    return o


def find_containing_triangle(dt, p, starting_triangle):
    # Walking algorithm
    containing_triangle = None
    current_triangle = dt[starting_triangle]
    while containing_triangle == None:
        visited_edges = 0
        for i in range(0, 3):
            edge_i = get_opposite_edge(current_triangle, i)
            if get_orientation(edge_i[0], edge_i[1], p) < 0:
                current_triangle = get_neighbour(dt, current_triangle, edge_i)
                break
            visited_edges += 1
        if visited_edges == 3:
            containing_triangle = current_triangle
    return current_triangle

def add_point(dt, p):
#    print("Searching containing triangle...")
    ct = find_containing_triangle(dt, p, 0)
    ct_index = get_triangle_index(dt, ct.id)

 #   print("Splitting into three new triangles")
    t1 = Triangle([p, ct.verts[0], ct.verts[1]], [])
    t2 = Triangle([p, ct.verts[1], ct.verts[2]], [])
    t3 = Triangle([p, ct.verts[2], ct.verts[0]], [])
    dt = np.append(dt, t1)
    dt = np.append(dt, t2)
    dt = np.append(dt, t3)
    dt = np.delete(dt, ct_index)
    
    # This sucks:
    dt = update_neighbours(dt)
    
    # It would be way faster to set the neighbours by hand:
    #t1.neighbours = [t2.id, t3.id] etc

    stack = np.array([t1, t2, t3])
    while stack.size > 0:
        
    return dt


def draw():
    points = tuple(map(tuple, np.random.rand(point_count, 2) * [w, h]))
    print("Generated " + str(point_count) + " sites")
    # We're doing iterative Delauny triangles

    # Start with a big triangle, add points one by one.
    scale = 2
    big_triangle = Triangle(
        [(0, h * -scale), (-w, h * scale), (w * scale, h * scale)], []
    )
    dt = np.array([big_triangle])

    for i, p in enumerate(points):
        print("Adding point " + str(i + 1) + "/" + str(point_count))
        dt = add_point(dt, p)

    draw_points(points)
    draw_triangles(dt)


size(w, h)
fill(0.95, 0.94, 0.93, 1)
rect(0, 0, w, h)
draw()

# saveImage(output_path + ts + ".png")
saveImage(output_path + "test" + ".png")
print("Done.")
