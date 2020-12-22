import pygame, sys

# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
# Initialize pygame engine
pygame.init()
# Set the caption and image for top bar of window
pygame.display.set_caption('Tower of Hanoi')
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('assets/signal-tower.png')
pygame.display.set_icon(icon)
# Custom Font
font = pygame.font.SysFont(None, 40)
black = 0, 0, 0
white = (255, 255, 255)

# This function takes parameters and draws a text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False

run = True


# Function for the main menu
def main_menu():
    while run:
        screen.fill((0, 0, 0))
        background = pygame.image.load('assets/Background Menu Image.png')

        screen.blit(background, (0, 0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        draw_text('Play Game', font, (255, 255, 255), screen, 50, 75)
        draw_text('Options', font, (255, 255, 255), screen, 50, 175)

        # Get Position of mouse
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(50, 110, 200, 50)
        button_2 = pygame.Rect(50, 210, 200, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (155, 93, 232), button_1)
        pygame.draw.rect(screen, (155, 93, 232), button_2)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


# Main game loop
def game():
    running = True
    while running:
        # Load Background Image
        background = pygame.image.load('assets/background (1).png')
        screen.blit(background, (0, 0))
        # Load Stick Images onto screen
        stick = pygame.image.load('assets/Stick_Object_1.png')
        screen.blit(background, (0, 0))
        screen.blit(stick, (320, 75))
        screen.blit(stick, (20, 75))
        screen.blit(stick, (620, 75))
        # Draw text
        draw_text('Game', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        # Main Game Loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_p:
                    pause()
        pygame.display.update()
        mainClock.tick(60)


# Options menu
def options():
    running = True
    x = 300
    x_btn = 425
    while running:
        # Load Background Image
        background = pygame.image.load('assets/menu.jpg')
        screen.blit(background, (0, 0))
        draw_text('Options', font, white, screen, 20, 20)
        draw_text('Choose the number of plates you want', font, white, screen, 150, 100)
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        draw_text('3 Disks - ', font, white, screen, x, 200)
        draw_text('4 Disks - ', font, white, screen, x, 300)
        draw_text('5 Disks - ', font, white, screen, x, 400)

        click = False
        # Button to generate the number of plates
        mark_x, mark_y = pygame.mouse.get_pos()

        button_1 = pygame.Rect(x_btn, 200, 25, 25)
        button_2 = pygame.Rect(x_btn, 300, 25, 25)
        button_3 = pygame.Rect(x_btn, 400, 25, 25)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if button_1.collidepoint((mark_x, mark_y)):
                if click:
                    draw_text('You chose 3 disks', font, white, screen, x-25, 450)
                    print('3')
                    pygame.display.update()
                    # Return 3
            if button_2.collidepoint((mark_x, mark_y)):
                if click:
                    draw_text('You chose 4 disks', font, white, screen, x-25, 450)
                    print('4')
                    # Return 4
            if button_3.collidepoint((mark_x, mark_y)):
                if click:
                    draw_text('You chose 5 disks', font, white, screen, x, 450)
                    print('5')
                    # Return 5

        pygame.draw.rect(screen, white, button_1)
        pygame.draw.rect(screen, white, button_2)
        pygame.draw.rect(screen, white, button_3)

        pygame.display.update()
        mainClock.tick(60)


# Pause menu screen
def pause():
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False

        draw_text('Paused', font, black, screen, 315, 50)

        draw_text('- Press C to continue.', font, black, screen, 250, 115)
        draw_text('- Press ESC to exit.', font, black, screen, 250, 145)

        pygame.display.update()
        mainClock.tick(5)


main_menu()

