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

score = 0
pause = False


# Color
WHITE = (255, 255, 255)

def player(x, y):
    screen.blit(playerImg, (x, y))


font_name  = pygame.font.match_font('arial')
def draw_text(surf_DT, text_DT, size_DT, x_DT, y_DT):
    font = pygame.font.Font(font_name, size_DT)
    text_surface = font.render(text_DT, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_DT , y_DT)
    surf_DT.blit(text_surface, text_rect)

def paused(surf_P, text_P, size_P, x_P, y_P):
    font = pygame.font.Font(font_name, size_P)
    text_surface = font.render(text_P, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_P, y_P)
    surf_P.blit(text_surface, text_rect)


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

        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_p:
                #pause = True






        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

        if event.type == pygame.MOUSEBUTTONUP:
            score = score +2
        elif event.type == pygame.MOUSEBUTTONDOWN:
            score = score + 1



    # RGB Sets background color for screen
    playerY += playerY_change
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 450 and 500:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    paused(screen, "Pause", 40, 300, 400)
    draw_text(screen, str(score), 30, 300, 10)
    player(playerX, playerY)
    pygame.display.update()