from cmu_graphics import *

class Tripwire:
    def __init__(self, orientation):
        self.color = 'red'
        self.orientation = orientation
    
    def __repr__(self):
        return 'Tripwire()'
    
    def draw(self, x, y, length):
        if self.orientation == 'horizontal':
            drawLine(x, y + length / 2, x + length, y + length / 2, fill = 'red', lineWidth=length/10)
        elif self.orientation == 'vertical':
            drawLine(x + length / 2, y, x + length / 2, y + length, fill = 'red', lineWidth=length/10)