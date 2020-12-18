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
white = 255, 255, 255
black = 0, 0, 0

# This function takes parameters and draws a text


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False


# Function for the main menu (1st window upon entering

# Main Menu (DO NOT TOUCH)


def main_menu():
    while True:

        screen.fill((0, 0, 0))
        background = pygame.image.load('assets/Background Menu Image.png')
        screen.blit(background, (0, 0))
        draw_text('Main Menu', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        mx, my = pygame.mouse.get_pos()
        # Draw text and button for entry to game function
        draw_text('Play Game', font, (255, 255, 255), screen, 50, 75)
        button_1 = pygame.Rect(50, 110, 200, 50)
        # Draw text and button for entry to options function
        button_2 = pygame.Rect(50, 210, 200, 50)
        draw_text('Options', font, (255, 255, 255), screen, 50, 175)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)

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

                elif event.key == K_ESCAPE:
                    running = False

        #screen.fill(white)

        draw_text('Paused', font, black, screen, 400, 300)

        draw_text('Press C to continue or Q to quit.', font, black, screen, 400, 350)

        pygame.display.update()
        mainClock.tick(5)


def game():
    running = True
    while running:
        # Load Background Image
        background = pygame.image.load('assets/background (1).png')
        screen.blit(background, (0, 0))
        draw_text('Game', font, (255, 255, 255), screen, 20, 20)
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_p:
                    #return running
                    pause()
        pygame.display.update()
        mainClock.tick(60)



def options():
    running = True
    while running:
        # Load Background Image
        background = pygame.image.load('assets/options.png')
        screen.blit(background, (0, 0))
        draw_text('Options', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        draw_text('Press ESC to exit', font, (255, 255, 255), screen, 20, 565)
        pygame.display.update()
        mainClock.tick(60)


main_menu()