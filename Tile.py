from tileTypes.Floor import *
class Tile:
    def __init__(self, x, y, xOffset, yOffset, length, tileType=Floor(), obj=None):
        self.type = tileType
        self.viewable = True
        self.x = x
        self.y = y
        self.xOffset = xOffset
        self.yOffset = yOffset
        self.length = length
        self.character = None
        self.obj = obj


    def setType(self, newType):
        self.type = newType 
    
    def draw(self):
        calculatedX = self.xOffset + (self.x * self.length)
        calculatedY =  self.yOffset + (self.y * self.length)
        self.type.drawTile(calculatedX, calculatedY, self.length)
        if self.character != None:
            self.character.draw(calculatedX, calculatedY)
        if self.obj != None:
            self.obj.draw(calculatedX, calculatedY, self.length)

    def changeCoords(self, newXOffset, newYOffset, newLength):
        self.xOffset = newXOffset
        self.yOffset = newYOffset
        self.length = newLength

    def __repr__(self):
        return f'Tile({self.x}, {self.y}, {self.xOffset}, {self.yOffset}, {self.length}, {self.type})'

