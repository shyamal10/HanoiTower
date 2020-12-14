import pygame
# Initialize program
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon on top of the window (Bar)s
pygame.display.set_caption("Tower of Hanoi")
icon = pygame.image.load('signal-tower.png')
pygame.display.set_icon(icon)

# Game Loop **ALL Components Go inside here for workflow**
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB Sets background color for screen
    screen.fill((51, 153, 204))
    pygame.display.update()
