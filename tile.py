from floor import *
class tile:
    def __init__(self):
        self.type = 0 # some sort of object 
        self.viewable = True
    def drawTile(self):
        if self.viewable:
           #  draw(self.type)
    def setType(self, newType):
        self.type = newType 