class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self. color = 'brown'
    def drawTile(self, length):
        drawRect(self.x, self.y, length, length)

