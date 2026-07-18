import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Custom Event")

white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)

sprite1 = pygame.Rect(150, 180, 100, 100)
sprite2 = pygame.Rect(390, 180, 100, 100)

color1 = red
color2 = blue

CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 2000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == CHANGE_COLOR:
            if color1 == red:
                color1 = blue
                color2 = red
            else:
                color1 = red
                color2 = blue

    screen.fill(white)

    pygame.draw.rect(screen, color1, sprite1)
    pygame.draw.rect(screen, color2, sprite2)

    pygame.display.update()