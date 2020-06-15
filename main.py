import pygame

# Initializing the PY-GAME
pygame.init()

# Creating Screen Window
screen = pygame.display.set_mode((800, 600))

# Title and Icon - Icon from https://www.flaticon.com/
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill values are RGB - Red green and blue
    screen.fill((0, 255, 0))
    pygame.display.update()

