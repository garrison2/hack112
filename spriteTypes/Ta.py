import PIL
import PIL.Image
from cmu_graphics import *
import os, pathlib
import random

imageFolder = "spriteTypes/imageFolder"

class Ta:
    def __init__(self, row, col, name, state, tileSize):
        self.row = row
        self.col = col
        self.name = name
        self.speed = 1
        self.state = state  
        self.FOV = []  
        self.width = tileSize * 0.8  
        self.height = tileSize * 0.8
        self.target = None
        self.image = Ta.openImage(f'imageFolder/{name}.png')

    @staticmethod
    def openImage(fileName):
        return CMUImage(PIL.Image.open(os.path.join(pathlib.Path(__file__).parent, fileName)))

    def drawSprite(self, boardLeft, boardTop, tileSize):

        x = boardLeft + self.col * tileSize + (tileSize - self.width) / 2
        y = boardTop + self.row * tileSize + (tileSize - self.height) / 2
        drawImage(self.image, x, y, width=65, height=65)

    def calculateFOV(self, rows, cols, fovRange=2):
        self.FOV = [
        (self.row + dr, self.col + dc)
        for dr in range(-fovRange, fovRange + 1)
        for dc in range(-fovRange, fovRange + 1)
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
            self.col += self.speed if dx > 0 else -self.speed
        elif dy != 0:  # Vertical movement
            self.row += self.speed if dy > 0 else -self.speed

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
                self.moveToward(player.row, player.col, grid)

    def patrol(self, grid, rows, cols):
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        random.shuffle(directions)

        for dr, dc in directions:
            new_row = self.row + dr
            new_col = self.col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != "wall":
                self.row = new_row
                self.col = new_col
                return 