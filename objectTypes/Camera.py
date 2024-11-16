from cmu_graphics import *

class Camera:
    
    def __init__(self, x, y, orientation):
        self.x = x
        self.y = y
        self. orientation = orientation
    
    def __repr__(self):
        return 'Camera()'

    def draw(self, x, y, length):
        drawCircle(x, y, length / 2, fill = None, border='red')