from cmu_graphics import *
from pyautogui import size
from sys import argv, path

from Tile import *
from spriteTypes import *

from tileTypes.Floor import *
from tileTypes.Door import *
from tileTypes.Wall import *
from objectTypes.Tripwire import *

try:
    from maps.map4 import map3 as gameMap
except ImportError:
    gameMap = None


def onAppStart(app):

    app.rows = 41
    app.cols = 41

    app.boardLeft = 0
    app.boardTop = 0
    app.boardWidth = 1000
    app.boardHeight = 1000

    if gameMap == None:
        app.board = [[None] * app.cols for row in range(app.rows)]

        for row in range(app.rows):
            for col in range(app.cols):
                app.board[row][col] = Tile(col, row, app.boardLeft, app.boardTop, app.boardWidth / app.cols)
    else:
        app.board = gameMap
     
    app.lastMouseCoords = (None, None)
    app.currentOrientation = 'horizontal'
    app.currentTileType = Floor()
    app.currentTileObject = None

def redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            cell = app.board[row][col]
            if isinstance(cell, Tile):
                cell.draw()
    iconX = app.width - 200
    iconY = app.height - 200
    if app.currentTileType != None:
        drawRect(iconX, iconY, 200, 200, fill=app.currentTileType.color)
        drawLabel(app.currentTileType, iconX + 100, iconY - 100, size=40)
    else:
        drawRect(iconX, iconY, 200, 200, fill=app.currentTileObject.color)
        drawLabel(app.currentTileObject, iconX + 100, iconY - 100, size=40)



def onMousePress(app, x, y):
    makeObject(app)
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows

    col, row = coordToIndex(x, y, cellWidth, cellHeight)
    if row < app.rows and col < app.cols:
        if app.currentTileType != None:
            app.board[row][col].type = app.currentTileType
        elif app.currentTileObject != None:
            app.board[row][col].object = app.currentTileObject


    app.lastMouseCoords = (x, y)
    
def onMouseRelease(app, x2, y2):
    makeObject(app)
    cellHeight = app.boardHeight/ app.rows
    cellWidth = app.boardWidth / app.cols

    x1, y1 = app.lastMouseCoords
    col1, row1 = int(x1 // cellWidth), int(y1 // cellHeight)
    col2, row2 = int(x2 // cellWidth), int(y2 // cellHeight)

    for row in range(min(row1, row2), max(row1, row2) + 1):
        for col in range(min(col1, col2), max(col1, col2) + 1):
            if row < app.rows and col < app.cols:
                if app.currentTileType != None:
                    app.board[row][col].type = app.currentTileType
                elif app.currentTileObject != None:
                    app.board[row][col].object = app.currentTileObject
            
def makeObject(app):
    key = app.key
    if key == 'F':
        app.currentTileType = Floor()
        app.currentTileObject = None
    elif key == 'W':
        app.currentTileType = Wall()
        app.currentTileObject = None
    elif key == 'O':
        app.currentTileType = Wall((157,174,17))
        app.currentTileObject = None
    elif key == 'D':
        app.currentTileType = Door()
        app.currentTileObject = None
    elif key == 'T':
        app.currentTileObject = Tripwire(app.currentOrientation)
        app.currentTileType = None
    elif key == 'r':
        if app.currentOrientation == 'horizontal':
            app.currentOrientation = 'vertical'
        else:
            app.currentOrientation = 'horizontal'
    elif key == 'S':
        saveMap(app)


def onKeyPress(app, key):
    app.key = key
    makeObject(app)

def saveMap(app):
    fileWritten = False
    num = 1
    while(not fileWritten):
        try:
            f = open(f"maps/map{num}.py", 'x')
            f.write("import sys\n")
            f.write("sys.path.append('../')\n")
            f.write(f'from cmu_graphics import *\n')
            f.write(f'from Tile import Tile\n')
            f.write(f'from tileTypes.Floor import Floor\n')
            f.write(f'from tileTypes.Wall import Wall\n')
            f.write(f'from tileTypes.Door import Door\n')
            f.write(f'map{num} = ')
            f.write(str(app.board))
            fileWritten = True
        except FileExistsError:
            num += 1



def coordToIndex(x, y, cellWidth, cellHeight):
    return (int(x // cellWidth), int(y // cellHeight))

def main():
    width, height = size()
    width = rounded(width * 3/4)
    height = rounded(height * 3/4)
    runApp(width=width, height=height)

main()

