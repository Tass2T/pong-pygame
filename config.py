import pygame
pygame.mixer.pre_init(44100, -16, 2,512)
pygame.init()
HEIGHT = 720
WIDTH = 1280
FRAMERATE = 60

# color list
lightGray = pygame.Color('gray56')
white = pygame.Color('white')

# font
font = pygame.font.Font("./assets/fonts/Minecraft.ttf", 60)

# sounds
plob_sound = pygame.mixer.Sound("./assets/sounds/pong.ogg")
score_sound = pygame.mixer.Sound("./assets/sounds/score.ogg")
