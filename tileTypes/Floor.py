from cmu_graphics import *

class Floor:
    def __init__(self):
        self. color = 'brown'
    def drawTile(self, x, y, length):
#        print(x, y)
        drawRect(x, y, length, length, fill=self.color, border='black')

