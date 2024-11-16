from cmu_graphics import *
from pyautogui import size
from tile import *
from tileTypes import *
from spriteTypes import *

def onAppStart(app):
    screenWidth, screenHeight = size()
    app.width = screenWidth
    app.height = screenHeight

    app.gridSize = min(app.width, app.height) * 0.8  # 80% of the smaller dimension
    app.boardLeft = (app.width - app.gridSize) / 2  # Center horizontally
    app.boardTop = (app.height - app.gridSize) / 2  # Center vertically


    app.rows = 10
    app.cols = 10
    app.tileSize = app.gridSize / app.rows
        
    app.board = [
        [
            Tile(
                x=app.boardLeft + col * app.tileSize,
                y=app.boardTop + row * app.tileSize,
                length=app.tileSize
            )
            for col in range(app.cols)
        ]
        for row in range(app.rows)
    ]
    app.Ta = Ta(0, 0, "philip", "patrolling")
    app.player = None  # Placeholder for player logic
    app.cameras = []  # Dynamic objects
 
def redrawAll(app):
    for row in app.board:
        for tile in row:
            tile.draw()
    for camera in app.cameras:
        camera.draw()

def placeObject(app, row, col, obj):
    """Places an object on the grid."""
    if row < 0 or row >= app.rows or col < 0 or col >= app.cols:
        return  # Out of bounds
    tile = app.board[row][col]
    tile.setType(obj)

def onMousePress(app, mouseX, mouseY):
    # Place a camera on the grid when the user clicks
    if app.boardLeft <= mouseX <= app.boardLeft + app.gridSize and \
       app.boardTop <= mouseY <= app.boardTop + app.gridSize:
        col = int((mouseX - app.boardLeft) / app.tileSize)
        row = int((mouseY - app.boardTop) / app.tileSize)
        placeObject(app, row, col, Camera())

screenWidth, screenHeight = size()
runApp(width=screenWidth, height=screenHeight)