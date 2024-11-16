from PIL import Image
import os
from cmu_graphics import *

imageFolder = "/Users/vishwa/Downloads/VSCode/hack112/spriteTypes/imageFolder"
fact = 40  

class Ta:
    def __init__(self, row, col, name, state, speed=1):
        self.row = row
        self.col = col
        self.name = name
        self.speed = speed
        self.state = state 
        self.FOV = []  
        self.image = Ta.makeCMUImage(f"{self.name}.png")  # Load sprite image
        self.width = fact * 0.8 
        self.height = fact * 0.8
        self.target = None  

    @staticmethod
    def makeCMUImage(name):
        imagePath = os.path.join(imageFolder, name)
        if not os.path.exists(imagePath):
            raise FileNotFoundError(f"Image {imagePath} not found.")
        pilImage = Image.open(imagePath)
        return CMUImage(pilImage)

    def drawSprite(self):
        # Calculate the top-left corner of the TA's sprite to center it in the grid cell
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
