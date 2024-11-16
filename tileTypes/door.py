class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self. color = 'grey'
    def drawTile(self, length):
        drawRect(self.x, self.y, length, length, color =self.color)
        drawline(self.x + length/2, self.y, self.x + length/2, self.y + length)
        drawline(self.x, self.y + length/2, self.x + length, self.y + length/2)

