import pygame,sys

def getInput(PlayerObject):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.scancode == 38: 
                pygame.quit()
                sys.exit()
            if event.scancode == 111: PlayerObject.direction = "UP"
            if event.scancode == 116: PlayerObject.direction = "DOWN"
        if event.type == pygame.KEYUP:
            if event.scancode == 111 and PlayerObject.direction == "UP": PlayerObject.direction = "NONE"
            if event.scancode == 116 and PlayerObject.direction == "DOWN": PlayerObject.direction = "NONE"
