from cmu_graphics import *
from pyautogui import size
from tile import *
from tileTypes import *
from spriteTypes import *
from PIL import image

#I PASTED IN TA Class BECASUSE THE "from tileTypes import *" would for some reason not bring in the ta class.

imageFolder = "/Users/vishwa/Downloads/VSCode/hack112/spriteTypes/imageFolder"
fact = 40  

class Ta:
    def __init__(self, row, col, name, state):
        self.row = row
        self.col = col
        self.name = name
        self.speed = 1
        self.state = state 
        self.FOV = []  
        self.width = fact * 0.8 
        self.height = fact * 0.8
        self.target = None  
        self.image = Ta.makeCMUImage(f'{self.name}.png')

    def makeCMUImage(name):
        image = imageFolder.open(f"images/{name}")
        return CMUImage(image)
    
    def drawSprite(self):
        x = self.col * fact + (fact - self.width) / 2
        y = self.row * fact + (fact - self.height) / 2
        drawImage(self.image, x, y, self.width, self.height)

    def calculateFOV(self, rows, cols, range=2):
        self.FOV = [
            (self.row + dr, self.col + dc)
            for dr in range(-range, range + 1)
            for dc in range(-range, range + 1)
            if 0 <= self.row + dr < rows and 0 <= self.col + dc < cols
        ]

    def detectPlayer(self, player):
        if player is None:
            return False
        return (player.row, player.col) in self.FOV

    def startChase(self, player):
        self.state = "chasing"
        self.target = player

    def patrol(self, grid, rows, cols):
        # Example: Move right until hitting the edge, then move down
        if self.col + 1 < cols:
            self.col += 1
        else:
            if self.row + 1 < rows:
                self.row += 1
                self.col = 0

    def moveToward(self, targetRow, targetCol):
        dx = targetCol - self.col
        dy = targetRow - self.row

        if abs(dx) > abs(dy):  # Move horizontally
            self.col += self.speed if dx > 0 else -self.speed
        elif dy != 0:  # Move vertically
            self.row += self.speed if dy > 0 else -self.speed

    def update(self, player, grid, rows, cols):
        self.calculateFOV(rows, cols)  # Recalculate FOV

        if self.state == "patrolling":
            if self.detectPlayer(player):
                self.startChase(player)  # Start chasing if player detected
            else:
                self.patrol(grid, rows, cols)  # Continue patrolling
        elif self.state == "chasing":
            if player is None:
                self.state = "patrolling"  # Return to patrolling if player disappears
                self.target = None
            else:
                self.moveToward(player.row, player.col)  # Move toward player





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
    app.Ta = Ta(0, 0, "phillip", "patrolling")
    app.player = None  # Placeholder for player logic
    app.cameras = []  # Dynamic objects
 
def redrawAll(app):
    for row in app.board:
        for tile in row:
            tile.draw()
    app.Ta.drawSprite()
    for Camera in app.cameras:
        Camera.draw()

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
        camera = Camera(row, col) 
        app.cameras.append(camera)  
        placeObject(app, row, col, camera)
screenWidth, screenHeight = size()
runApp(width=screenWidth, height=screenHeight)