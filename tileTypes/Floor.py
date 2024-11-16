from cmu_graphics import *

class Floor:
    def __init__(self):
        self. color = 'blue'
    def __repr__(self):
        return 'Floor()'
    def drawTile(self, x, y, length):
        drawRect(x, y, length, length, fill=self.color, border='black')

