from tileTypes.floor import *
from spriteTypes.ta import*

class Tile:
    def __init__(self, type, character):
        self.type = type # some sort of object 
        self.character = character
        self.viewable = None
    def drawTile(self):
        if self.viewable:
           #  draw(self.type) 
           pass 
    def setType(self, newType):
        self.type = newType 

    def isViewable(self):
        pass

board = [Tile(Floor(), TA())]