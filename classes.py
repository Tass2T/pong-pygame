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

    def checkForCollision(self, playerRect,opponentRect):
        # collision with walls
        if self.rect.y >= config.HEIGHT or self.rect.y <= 0: self.reverse_y()
        if self.rect.x >= config.WIDTH or self.rect.x <= 0: self.reverse_x()
        # collisions with player or opponent
        if pygame.Rect.colliderect(self.rect, playerRect): self.reverse_x()
        if pygame.Rect.colliderect(self.rect, opponentRect): self.reverse_x()

    def reverse_x(self):
        self.speed_x *= -1

    def reverse_y(self):
        self.speed_y *= -1