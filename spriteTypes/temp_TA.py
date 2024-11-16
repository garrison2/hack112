class TA:
    def __init__(self,name,speed = default,x,y):
        self.x = x
        self.y = y
        self.name = name
        self.speed = speed
        self.state = 'patrolling'
        self.FOV = something
    
    def draw(self,x,y):
        
    def detectPlayer(self,player):
        if (player.x,player.y) in self.FOV:
            self.startChase(self,player)

    def startChase(self,player):
        #move to player
        
