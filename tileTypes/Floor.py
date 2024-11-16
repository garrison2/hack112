from cmu_graphics import *

class Floor:
    def __init__(self, fill=(255, 255, 255)):
        self.rgbVals = fill
        self.color = rgb(self.rgbVals[0], self.rgbVals[1], self.rgbVals[2])
    def __repr__(self):
        return 'Floor()'
    def drawTile(self, x, y, length):
        drawRect(x, y, length, length, fill=self.color, border='black')

