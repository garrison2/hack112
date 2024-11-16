class Camera:
    def __init__(self, row, col, length=40, detectionRange=2):
        self.row = row
        self.col = col
        self.length = length
        self.detectionRange = detectionRange  # Detection radius in tiles
        self.color = "red"

    def draw(self):
        x = self.col * self.length
        y = self.row * self.length
        drawRect(x, y, self.length, self.length, fill=self.color, border="black")

    def detectPlayer(self, player, rows, cols):
        if player is None:
            return False
        distance = abs(player.row - self.row) + abs(player.col - self.col)
        return distance <= self.detectionRange

    def triggerAlarm(self):
        print("Alarm! Player detected by camera!")
 