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

def onKeyPress(app,key):
    if key == 'up':
        player.moveUp()
    elif key == 'down':
        player.moveDown()
    elif key == 'right':
        player.moveRight()
    elif key == 'left':
        player.moveLeft

def onKeyHold(key):
    if key == 'up':
        moveUp(app,player)
    elif key == 'down':
        moveDown(app,player)
    elif key == 'right':
        moveRight(app,player)
    elif key == 'left':
        moveLeft(app,player)

def moveRight(app,character):
        if (character.xIndex + 1 < app.board.length() 
            and app.board[character.xIndex + 1].character == None):
            app.board[character.xIndex][character.yIndex].character = None
            app.board[character.xIndex+1][character.yIndex].character = character


def moveLeft(app,character):
    if (character.xIndex - 1 > -1 
        and app.board[character.xIndex - 1].character == None):
        app.board[character.xIndex][character.yIndex].character = None
        app.board[character.xIndex-1][character.yIndex].character = character

def moveUp(app,character):
        if (character.yIndex - 1 > -1
            and app.board[character.yIndex - 1].character == None):
            app.board[character.xIndex][character.yIndex].character = None
            app.board[character.xIndex][character.yIndex-1].character = character

def moveDown(app,character):
        if (character.yIndex + 1 < app.board.length() 
            and app.board[character.xIndex + 1].character == None):
            app.board[character.xIndex][character.yIndex].character = None
            app.board[character.xIndex][character.yIndex+1].character = character


def main():
    width, height = size()
    width = rounded(width * 3/4)
    height = rounded(height * 3/4)
    runApp(width=width, height=height)

main()
