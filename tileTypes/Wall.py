from cmu_graphics import *

class Wall:
    def __init__(self, fill=(187, 178, 168)):
        self.rgbVals = fill
        self.color = rgb(self.rgbVals[0], self.rgbVals[1], self.rgbVals[2])
    def __repr__(self):
        return f'Wall({self.rgbVals})'
    def drawTile(self, x, y, length):
        drawRect(x, y, length, length, fill=self.color, border='black')

