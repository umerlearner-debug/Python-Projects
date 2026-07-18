import math
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("space.jpg")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_image = pygame.image.load("images.jpg")
player_x = PLAYER_START_X
player_y = PLAYER_START_Y
player_x_change = 0

enemy_Img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_Img.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)


bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_CHANGE = 0
bulletY_CHANGE = BULLET_SPEED_Y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

overfont = pygame.font.Font("freesansbold.ttf", 64)