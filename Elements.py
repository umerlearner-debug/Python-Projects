import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)

font = pygame.font.SysFont(None, 36)
text = font.render("Welcome to My Game", True, black)

text_rect = text.get_rect(center=(320, 100))

rect = pygame.Rect(220, 170, 200, 120)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)

    pygame.draw.rect(screen, blue, rect)

    screen.blit(text, text_rect)

    pygame.display.update()