import math
import pygame
import random

SCREEN_WIDTH = 500
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

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("space.jpg")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

player_image = pygame.transform.scale(pygame.image.load('player.png'), (50, 50))
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
    scaled_enemy = pygame.transform.scale(pygame.image.load('ufo.png'), (50, 50))
    enemy_Img.append(scaled_enemy)
    enemy_x.append(random.randint(0, SCREEN_WIDTH - 64))
    enemy_y.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemy_x_change.append(ENEMY_SPEED_X)
    enemy_y_change.append(ENEMY_SPEED_Y)


bulletImg = pygame.image.load("bullet.jpg") 
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

def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (255, 255, 255) )
    screen.blit(score, (x, y))

def game_over_text():
    over_text = overfont.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(player_image, (x, y))

def enemy(x, y, i):
    screen.blit(enemy_Img[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE


running = True
while running: 
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_RIGHT:
                        player_x_change = 5
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    bulletX = player_x
                    fire_bullet(bulletX, bulletY)
            if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_x_change = 0

    player_x += player_x_change
    player_x = max(0, min(player_x, SCREEN_WIDTH - 64))

    for i in range(num_of_enemies):
        if enemy_y[i] > 340: # Game Over Condition
            for j in range(num_of_enemies):
                enemy_y[j] = 2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= SCREEN_WIDTH - 64:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]
        if isCollision(enemy_x[i], enemy_y[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemy_x[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
        enemy(enemy_x[i], enemy_y[i], i)
    if bulletY <= 0:
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_CHANGE
    player(player_x, player_y)
    show_score(textX, textY)
    pygame.display.update()
        

