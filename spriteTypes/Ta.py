from PIL import image
from cmu_graphics import *

class ta:
    philip = "phillip.png"
    varun = "varun.png"
    dragon3 = "dragon3.png"
    def __init__(self, x, y, taName):
        self.x = x
        self.y = y  
        self.image = ta.makeCMUImage(f'{taName}.png')

    def makeCMUImage(name):
        image = imageFolder.open(f"images/{name}")
        return CMUImage(image)

    def drawSprite(self):
        drawImage(self.image, self.x, self.y, self.width, self.height)
