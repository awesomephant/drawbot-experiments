from drawbot_skia.drawbot import *
import math


def fillet(x, y, w, h, angle=45, ratio=.5):
    with savedState():
        # We're going to rotate around the centre of the fillet
        translate(x, y)
        rotate(angle, (w / 2, h / 2))
        path = BezierPath()
        path.moveTo((0, h))
        path.curveTo((w * ratio, h), (w, h * ratio), (w, 0))
        path.lineTo((w, h))
        path.lineTo((0, h))
        path.closePath()
        drawPath(path)
