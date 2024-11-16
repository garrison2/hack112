from PIL import image

class ta:
    philip = "phillip.png"
    varun = "varun.png"
    dragon3 = "dragon3.png"
    def __init__(self, row, col, name, state, speed=10):
        self.x = col * fact
        self.y = row * fact
        self.name = name
        self.speed = speed
        self.state = f'{state}' #patrolling
        self.FOV = None
        self.image = ta.makeCMUImage(f'{self.name}.png')

    def makeCMUImage(name):
        image = imageFolder.open(f"images/{name}")
        return CMUImage(image)

    def drawSprite(self):
        drawImage(self.image, self.x, self.y, self.width, self.height)

    def detectPlayer(self,player):
        if (player.x,player.y) in self.FOV:
            self.startChase(self,player)

    def startChase(self,player):
        #move to player