from tile_types.floor import *
from sprite_types.ta import*

class Tile:
    def __init__(self, type, character):
        self.type = type # some sort of object 
        self.character = character
        self.viewable = isViewable(self)
    def drawTile(self):
        if self.viewable:
           #  draw(self.type) 
           pass 
    def setType(self, newType):
        self.type = newType 

    def isViewable(self):
        pass

board = [Tile(Floor(), TA())]