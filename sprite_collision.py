import pygame 
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400

MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("game.jpg"),(SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.SysFont("TIMES NEW ROMAN", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, colour, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodger blue'))

        pygame.draw.rect(self.image, color, pygame.Rect(0,0, width, height))

        self.rect = self.image.get_rect()
    
    def move(self, x_change, y_change):
        self.rect.x = max(
            min(self.rect.x + x_change, SCREEN_WIDTH - self.rect.width), 0)
        

        self.rect.y = max(
            min(self.rect.y + x_change, SCREEN_HEIGHT - self.rect.height), 0)
        

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites = pygame.sprite.Group()

sprite1 = Sprite(pygame.color('black'), 20, 30)
sprite1.rect.x, sprite1.rect.y = random.randint(
    0, SCREEN_WIDTH - sprite1.rect.width, random.randint(
        0, SCREEN_HEIGHT - sprite1.rect.height, random.randint
    ))

all_sprites.add(sprite1)