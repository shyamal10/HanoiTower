import pygame
# Initialize program
pygame.init()

# Create game screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background (1).png')

# Title and Icon on top of the window (Bar)s
pygame.display.set_caption("Tower of Hanoi")
icon = pygame.image.load('penguin.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Blue_disk.png')
playerX = 200
playerY = 200
playerX_change = 0
playerY_change = 0


def player(x , y):
    screen.blit(playerImg, (x, y))

# Game Loop **ALL Components Go inside here for workflow**
running = True
while running:

    screen.fill((255, 153, 153))
    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change = -0.2
            if event.key == pygame.K_DOWN:
                playerY_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0



    # RGB Sets background color for screen
    playerY += playerY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 280:
        playerY = 280

    player(playerX, playerY)
    pygame.display.update()