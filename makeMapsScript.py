from cmu_graphics import *
from pyautogui import size

from Tile import *
from spriteTypes import *

from tileTypes.Floor import *
from tileTypes.Door import *
from tileTypes.Wall import *

def onAppStart(app):
    #    app.background = 'black'

    app.rows = 20
    app.cols = 20

    app.boardLeft = 0
    app.boardTop = 0
    app.boardWidth = 1000
    app.boardHeight = 1000
    app.board = [[None] * app.cols for row in range(app.rows)]

    for row in range(app.rows):
        for col in range(app.cols):
            app.board[row][col] = Tile(col, row, app.boardLeft, app.boardTop, app.boardWidth / app.cols)
 
    app.lastMouseCoords = (None, None)
    app.currentKeyTile = Floor()

def redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            cell = app.board[row][col]
            if isinstance(cell, Tile):
                cell.draw()
    iconX = app.width - 200
    iconY = app.height - 200
    drawRect(iconX, iconY, 200, 200, fill=app.currentKeyTile.color)
    drawLabel(app.currentKeyTile, iconX + 100, iconY - 100, size=40)


def onMousePress(app, x, y):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows

    col, row = coordToIndex(x, y, cellWidth, cellHeight)
    if row < app.rows and col < app.cols:
        print(type(app.board[row][col].type), app.board[row][col].type.color)
        app.board[row][col].type = app.currentKeyTile

    app.lastMouseCoords = (x, y)
    
def onMouseRelease(app, x2, y2):
    cellHeight = app.boardHeight/ app.rows
    cellWidth = app.boardWidth / app.cols

    x1, y1 = app.lastMouseCoords
    col1, row1 = int(x1 // cellWidth), int(y1 // cellHeight)
    col2, row2 = int(x2 // cellWidth), int(y2 // cellHeight)

    for row in range(min(row1, row2), max(row1, row2) + 1):
        for col in range(min(col1, col2), max(col1, col2) + 1):
         if row < app.rows and col < app.cols:
            app.board[row][col].type = app.currentKeyTile

def onKeyPress(app, key):
    if key == 'up':
        app.cols += 1
        app.rows += 1
        if len(app.board) < app.rows:
            for col in range(app.cols):
                xPos = app.boardLeft + (app.boardWidth / app.cols) * col
                yPos = app.boardTop + (app.boardHeight / app.rows) * (app.rows - 1) 
                app.board.append(Tile(xPos, yPos, app.boardWidth /app.cols))

        if len(app.board[0]) < app.cols:
            for row in range(app.rows):
                if len(app.board[row]) < app.cols:
                    xPos = app.boardLeft + (app.boardWidth / app.cols) * (app.cols - 1)
                    yPos = app.boardTop + (app.boardHeight / app.rows) * row
                    app.board.append(Tile(xPos, yPos, app.boardWidth /app.cols))




    elif key == 'F':
        app.currentKeyTile = Floor()
    elif key == 'W':
        print('Wall')
        app.currentKeyTile = Wall()
    elif key == 'O':
        app.currentKeyTile = Wall((157,174,17))
    elif key == 'D':
        print('Door')
        app.currentKeyTile = Door()
    elif key == 'S':
        saveMap(app)

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

