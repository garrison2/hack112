from tileTypes.Floor import *
class Tile:
    def __init__(self, x, y, length, tileType=Floor()):
        self.type = tileType
        self.viewable = True
        self.x = x
        self.y = y
        self.length = length
        self.character = None


    def setType(self, newType):
        self.type = newType 
    
    def draw(self):
        self.type.drawTile(self.x, self.y, self.length)
        if self.character != None:
            self.character.draw(self.x, self.y)

    def __repr__(self):
        return f'Tile({self.x}, {self.y}, {self.length}, {self.type})'

