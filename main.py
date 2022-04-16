import pygame, config, classes, inputs

pygame.init()
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# main surface
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

# rects
mainRect = pygame.Rect(0,0,config.WIDTH, config.HEIGHT)
player = classes.Player()
opponent = classes.Opponent()
ball = classes.Ball()

while True:
    # get inputs
    inputs.getInput(player)

    # prepare dialogue
    playerScore = config.font.render(str(player.score), True, config.white)
    opponentScore = config.font.render(str(opponent.score), True, config.white)

    # move and update
    ball.move()
    player.move()
    opponent.defineDirection(ball)
    opponent.move()
    ball.checkForCollision(player, opponent)

    # drawings here 
    screen.fill(config.lightGray)
    screen.blit(playerScore, (int(config.WIDTH/2-50), 15))
    screen.blit(opponentScore, (int(config.WIDTH/2+20), 15))
    pygame.draw.ellipse(screen, config.white, ball.rect)
    pygame.draw.rect(screen,config.white, player.rect)
    pygame.draw.rect(screen, config.white, opponent.rect)
    pygame.draw.aaline(screen, config.white, (config.WIDTH/2, 0), (config.WIDTH/2, config.HEIGHT))

    pygame.display.flip()
    clock.tick(config.FRAMERATE)
