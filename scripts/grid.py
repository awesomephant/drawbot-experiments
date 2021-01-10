from drawbot_skia.drawbot import *
from fillet import fillet
import random
import datetime
import math
import csv

# Configuration
output_path = '../output'
padding = 0
margin = 50
grid = []
w = 1900
h = 1300


with open('../input/10x15.csv', newline='') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        newRow = []
        for num in row:
            newRow.append(int(float(num)))
        grid.append(newRow)


def draw(grid, s, offset_x, offset_y):
    rows = len(grid)
    cols = len(grid[0])
    fs = .45
    filletRatio = 1
    radius = 0
    filletSize = s * fs
    for row in range(rows):
        for col in range(cols):
            if(grid[row][col] == 1):
                x = (s * col) + margin + offset_x
                y = h - (s * (row + 1)) - margin + offset_y
                rect(x, y, s - padding, s - padding)
    for row in range(rows):
        for col in range(cols):
            x = (s * col) + margin + offset_x
            y = h - (s * (row + 1)) - margin + offset_y
            if (row < rows - 1 and col < cols - 1 and grid[row + 1][col] == 1 and grid[row][col + 1] and grid[row][col] == 0):
                fillet(x + (s - filletSize), y,
                       filletSize, filletSize, -90, filletRatio)
            if (row < rows - 1 and col > 0 and grid[row][col - 1] == 1 and grid[row + 1][col] and grid[row][col] == 0):
                fillet(x, y, filletSize, filletSize, 180, filletRatio)
            if (row > 0 and col > 0 and grid[row][col - 1] == 1 and grid[row - 1][col] and grid[row][col] == 0):
                fillet(x, y + (s - filletSize), filletSize,
                       filletSize, 90, filletRatio)
            if (row > 0 and col < cols - 1 and grid[row][col + 1] == 1 and grid[row - 1][col] and grid[row][col] == 0):
                fillet(x + (s - filletSize), y + (s - filletSize),
                       filletSize, filletSize, 0, filletRatio)

print(str(len(grid[0])) + "x" + str(len(grid)) + " grid found.")

newPage(w, h)

fill(.97, .99, .95)
rect(0,0,w,h)

blendMode('multiply')

fill(1.0, .01, .10)
draw(grid, 100, 100, 00)

fill(0.02, 1.0, .03)
draw(grid, 100, 0, -100)

fill(.01, .02, 1.0)
draw(grid, 100, 100, -200)

saveImage(output_path + "/test" + ".png")
