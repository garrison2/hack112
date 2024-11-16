from cmu_graphics import *
from pyautogui import size
from tile import *
from tileTypes import *
from spriteTypes import *

def onAppStart(app):

    app.rows = 10
    app.cols = 10
    screenWidth, screenHeight = size()
    app.boardWidth = screenHeight
    app.boardHeight = screenHeight
    app.boardLeft = screenWidth / 2 - app.boardWidth / 2
    app.boardTop = 0
    app.board = []
    for i in range(app.rows):
        app.board.append([])
        for j in range(app.cols):
            app.board[i].append(None)
    for row in range(app.rows):
        for col in range(app.cols):
            xPos = app.boardLeft + (app.boardWidth / app.cols) * col
            yPos = app.boardTop + (app.boardHeight / app.rows) * row
            app.board[row][col] = Tile(xPos, yPos, app.boardWidth / app.cols)
            print(app.board[row][col].x, app.board[row][col].y)
    for rows in app.board:
        for cell in rows:
            print(cell.x, cell.y)
    print('______________________________-')

def redrawAll(app):
    for row in range(app.rows):
        for col in range(app.cols):
            cell = app.board[row][col]
            print(app.board[row][col].x, app.board[row][col].y)
            if isinstance(cell, Tile):
#                print(row, col, cell.x, cell.y)
                cell.draw()

def main():
    width, height = size()
    runApp(width=width, height=height)

main()