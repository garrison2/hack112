from cmu_graphics import *

class Door:
    def __init__(self):
        self. color = 'grey'
    def __repr__(self):
        return 'Door()'
    def drawTile(self, x, y, length):
        drawRect(x, y, length, length, fill=self.color)
        drawLine(x + length/2, y, x + length/2, y + length)
        drawLine(x, y + length/2, x + length, y + length/2)

