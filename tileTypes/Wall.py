class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self. color = 'black'
    def drawTile(self, length):
        drawRect(self.x, self.y, length, length, color = self.color)

