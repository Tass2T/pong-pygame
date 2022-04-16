import config, pygame

class Player:
    def __init__(self):
        self.height = 140
        self.width = 20
        self.posX = 15
        self.posY = int(config.HEIGHT/2-self.height/2)
        self.rect = pygame.Rect(self.posX, int(config.HEIGHT/2-self.height/2), self.width, self.height)
        self.direction = "NONE"
        self.score = 0

    def move(self):
        if self.direction == "UP" and self.rect.y > 0: self.rect.y -= 7
        if self.direction == "DOWN" and self.rect.y < config.HEIGHT - self.height: self.rect.y += 7

class Opponent:
    def __init__(self):
        self.height = 140
        self.width = 20
        self.posX = int(config.WIDTH-(self.width + 15))
        self.posY = int(config.HEIGHT/2-(self.height/2))
        self.rect = pygame.Rect(int(config.WIDTH-35), int(config.HEIGHT/2-self.height/2), self.width, self.height)
        self.direction = "NONE"
        self.score = 0
    
    def defineDirection(self, ballObject):
        if ballObject.rect.top - ballObject.height/2 < self.rect.top:
            self.direction ="UP"
        elif ballObject.rect.top - ballObject.height/2  > self.rect.bottom:
            self.direction ="DOWN"
        else:
            self.direction ="NONE"

    def move(self):
        if self.direction == "UP" and self.rect.y > 0: self.rect.y -= 7
        if self.direction == "DOWN" and self.rect.y < config.HEIGHT - self.height: self.rect.y += 7

class Ball:
    def __init__(self):
        self.height = 20
        self.width = 20
        self.rect = pygame.Rect(int(config.WIDTH/2-10), int(config.HEIGHT/2-10), self.width,self.height)
        self.speed_y = 7
        self.speed_x = 7

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def resetPos(self):
        self.rect.y = config.HEIGHT / 2
        self.rect.x = config.WIDTH / 2

    def checkForCollision(self, player,opponent):
        # collision with walls
        if self.rect.y >= config.HEIGHT or self.rect.y <= 0: self.reverse_y()
        
        if self.rect.x <= 10: 
            opponent.score += 1
            self.resetPos()
        if self.rect.x >= config.WIDTH - 30: 
            player.score += 1
            self.resetPos()
        
        # collisions with player or opponent
        if pygame.Rect.colliderect(self.rect, player.rect): self.reverse_x()
        if pygame.Rect.colliderect(self.rect, opponent.rect): self.reverse_x()

    def reverse_x(self):
        self.speed_x *= -1

    def reverse_y(self):
        self.speed_y *= -1