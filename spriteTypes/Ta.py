import PIL
import PIL.Image
from cmu_graphics import *
import os, pathlib

imageFolder = "spriteTypes/imageFolder"
# imageFolder = ["cmu://856355/35005325/phillip.png", "cmu://856355/35005331/tiffany.png", "cmu://856355/35005335/varun.png"]
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
        self.image = Ta.openImage(f'imageFolder/{name}.png')
        # if name == 'varun':
        #     self.image =  imageFolder[2]
        # elif name == 'phillip':
        #     self.image =  imageFolder[0]
        # else:
        #     self.image =  imageFolder[1]

    def openImage(fileName):
        return CMUImage(PIL.Image.open(os.path.join(pathlib.Path(__file__).parent,fileName)))

    def drawSprite(self):
        x = self.col * fact + (fact - self.width) / 2
        y = self.row * fact + (fact - self.height) / 2
        print(self.image)
        drawImage(self.image, x, y)
        

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
        if self.col + 1 < cols:
            self.col += 1
        else:
            if self.row + 1 < rows:
                self.row += 1
                self.col = 0

    def moveToward(self, targetRow, targetCol, grid):
        dx = targetCol - self.col
        dy = targetRow - self.row
        if abs(dx) > abs(dy):  # Prioritize horizontal movement
            nextCol = self.col + (self.speed if dx > 0 else -self.speed)
            if grid[self.row][nextCol] != 'wall':  # Check for walls
                self.col = nextCol
        elif dy != 0:  # Vertical movement
            nextRow = self.row + (self.speed if dy > 0 else -self.speed)
            if grid[nextRow][self.col] != 'wall': 
                self.row = nextRow


    def update(self, player, grid, rows, cols):
        self.calculateFOV(rows, cols)

        if self.state == "patrolling":
            if self.detectPlayer(player):  
                self.startChase(player)  
            else:
                self.patrol(grid, rows, cols)  

        elif self.state == "chasing":
            if player is None:  
                self.state = "patrolling"  
                self.target = None
            else:
                if self.detectPlayer(player):
                    self.moveToward(player.row, player.col, grid)
                else:
                    self.state = "patrolling"
                    self.target = None
