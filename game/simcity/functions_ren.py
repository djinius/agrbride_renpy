"""renpy
init -1 python:
"""

def calcXYPos(x, y, zoom=1.):
    global srpgXMax
    if y % 2 == 0:
        xp = 256 + 256 * x
    else:
        xp = 128 + 256 * x
    yp = 256 * y + 512

    return (int(xp * zoom), int(yp * zoom))

def evenR2Cube(row, col):
    x = col - (row + 1) // 2
    z = row
    y = -x - z

    return (x, y, z)

def getColLimit(x, y):
    if y % 2 == 0:
        return x - 1
    else:
        return x


def citySize(cells, zoom):
    return (int(cells[0]*256*zoom), int(cells[1]*256*zoom))

def cityMinZoom(cells=(15, 7)):
    return config.screen_width / (cells[0] * 256)

def initializeCity():
    global buildings
    global cityCells

    cols = cityCells[0]
    rows = cityCells[1]

    for y in range(0, cityCells[1]):
        arow = []

        for x in range(0, cityCells[0]):
            arow.append(None)

        buildings.append(arow)

    buildings[0][cols//2 - 2] = "lodge"
    buildings[0][cols//2 - 1] = False
    buildings[0][cols//2    ] = "maintree"
    buildings[0][cols//2 + 1] = False
    buildings[0][cols//2 + 2] = "barn"

def addBuilding(x, y, bd):
    global buildings
    buildings[y][x] = bd