from tile_types.floor import *
class tile:
    def __init__(self):
        self.type = Floor # some sort of object 
        self.viewable = True
    def drawTile(self):
        if self.viewable:
           #  draw(self.type)
    def setType(self, newType):
        self.type = newType 