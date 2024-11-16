from cmu_graphics import *
from tileTypes import *
from spriteTypes import *

def onAppStart(app):
    app.rows = 10
    app.cols = 10
    app.boardLeft = 20
    app.boardTop = 10
    app.boardWidth = 300
    app.boardHeight = 300
    app.board = [[None] * app.rows] * app.cols
    for row in range(app.rows):
        for col in range(app.cols):
            xPos = app.boardLeft + (app.boardWidth / app.cols) * col
            yPos = app.boardTop + (app.boardHeight / app.rows) * row
            app.board[row][col] = Tile(xPos, yPos,app.boardWidth / app.cols)

def test():
    pass

def redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            cell = app.board[row][col]
            if isinstance(cell, Tile):
                cell.draw()


runApp()