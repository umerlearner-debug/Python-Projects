import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My first game screen")

bg_color = (58, 58, 58)

image = pygame.image.load("penguin.jpg")

image = pygame.transform.scale(image, (300, 300))

x = 100
y = 100

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(bg_color)

    screen.blit(image, (x, y))

    pygame.display.update()

pygame.quit()