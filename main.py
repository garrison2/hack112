from cmu_graphics import *
from pyautogui import size
from tile import *
from tileTypes import *
from spriteTypes.Ta import *


from cmu_graphics import *
from pyautogui import size
from tile import *
from tileTypes import *
from spriteTypes.Ta import Ta

def onStep(app):
    if app.TA.state == "patrolling":
        app.TA.update(None, app.board, app.rows, app.cols)



def onAppStart(app):
    screenWidth, screenHeight = size()
    app.width = screenWidth
    app.height = screenHeight
    app.stepsPerSecond = 1

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
    app.TA = Ta(0, 0, "varun", "patrolling", app.tileSize)  
    app.player = None  
    app.cameras = []  


def redrawAll(app):
    for row in app.board:
        for tile in row:
            tile.draw()
    app.TA.drawSprite(app.boardLeft, app.boardTop, app.tileSize)

    # Temporarily disable camera rendering
    # for camera in app.cameras:
    #     camera.draw()


def onMousePress(app, mouseX, mouseY):
    if app.boardLeft <= mouseX <= app.boardLeft + app.gridSize and \
       app.boardTop <= mouseY <= app.boardTop + app.gridSize:
        col = int((mouseX - app.boardLeft) / app.tileSize)
        row = int((mouseY - app.boardTop) / app.tileSize)
        app.TA.row = row
        app.TA.col = col

    # Temporarily disable camera placement
    # camera = Camera(row, col)
    # app.cameras.append(camera)
    # placeObject(app, row, col, camera)

def onKeyPress(app, key):
    if key == 'a':
        app.TA.name = 'varun'
    elif key == 's':
        app.TA.name = 'phillip'
    elif key == 'd': 
        app.TA.name = 'tiffany'
    else:
        print(f"Key '{key}' does not correspond to a TA.")
    
    app.TA.image = Ta.openImage(f'imageFolder/{app.TA.name}.png')



def placeObject(app, row, col, obj):
    """Places an object on the grid."""
    if row < 0 or row >= app.rows or col < 0 or col >= app.cols:
        return  
    tile = app.board[row][col]
    tile.setType(obj)

screenWidth, screenHeight = size()
runApp(width=screenWidth, height=screenHeight)