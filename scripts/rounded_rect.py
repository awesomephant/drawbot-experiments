from drawbot_skia.drawbot import *
import math

def rounded_rect(x, y, w, h, r, ratio=.3):
    path = BezierPath()
    path.moveTo((x, y + r))
    path.lineTo((x, y + h - r))
    path.curveTo((x, y + h - (r * ratio)),
                 (x + (r * ratio), y + h), (x + r, y + h))
    path.lineTo((x + w - r, y + h))
    path.curveTo((x + w - (r * ratio), y + h),
                 (x + w, y + h - (r * ratio)), (x + w, y + h - r))
    path.lineTo((x + w, y + r))
    path.curveTo((x + w, y + (r * ratio)),
                 (x + w - (r * ratio), y), (x + w - r, y))
    path.lineTo((x + r, y))
    path.curveTo((x + (r * ratio), y), (x, y + (r * ratio)), (x, y + r))
    path.closePath()
    drawPath(path)
