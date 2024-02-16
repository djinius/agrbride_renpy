"""renpy
init -1 python:
"""

def calcXYPos(x, y, zoom=1.):
    global srpgXMax
    if y % 2 == 0:
        xp = 384 + 256 * x
    else:
        xp = 256 + 256 * x
    yp = 256 * y + 320

    return (int(xp * zoom), int(yp * zoom))

def evenR2Cube(row, col):
    x = col - (row + 1) // 2
    z = row
    y = -x - z

    return (x, y, z)

