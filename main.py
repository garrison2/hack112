from cmu_graphics import *
from pyautogui import size
from Tile import *
from tileTypes import *
from spriteTypes import *
from maps import *

from maps.map1 import map1 as gameMap

def onAppStart(app):
    app.background = 'black'
    app.rows = 20
    app.cols = 20

    setElements(app)


def setElements(app):
    squareDimensions = min(app.width, app.height)
    app.boardLeft = (app.width - squareDimensions)/2
    app.boardTop = (app.height - squareDimensions)/2
    app.boardWidth = squareDimensions
    app.boardHeight = squareDimensions
    app.board = [[None] * app.cols for row in range(app.rows)]

   
    app.board = gameMap
    for row in range(app.rows):
        for col in range(app.cols):
            app.board[row][col].changeCoords(app.boardLeft, app.boardTop, app.boardWidth / app.cols)
 


def redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            cell = app.board[row][col]
            if isinstance(cell, Tile):
                cell.draw()

def main():
    width, height = size()
    width = rounded(width * 3/4)
    height = rounded(height * 3/4)
    runApp(width=width, height=height)

main()
