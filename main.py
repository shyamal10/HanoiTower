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
# Global variables used throughout the program
number_of_plates = 3
minimumMoves = 7
score = 0
user_choice = 3
rectangle = pygame.rect.Rect(40, 508, 100, 25)
rectangle_draging = False

rectangle2 = pygame.rect.Rect(55, 481, 65, 25)
rectangle3 = pygame.rect.Rect(73, 453.5, 30, 25)
stick_bottom_y = 75

# Calculate and return min number of moves needed
def min_moves(num):
    # min number of moves = (2^n) - 1, n = number of plates
    return (2**num) - 1


# This function takes parameters and draws a text
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


click = False
run = True
pauseQuit = False


# Function for the main menu
def main_menu():
    while run:
        screen.fill((0, 0, 0))
        background = pygame.image.load('assets/Background Menu Image.png')

        screen.blit(background, (0, 0))
        draw_text('Main Menu', font, white, screen, 20, 20)
        draw_text('Press ESC to exit', font, white, screen, 20, 565)
        draw_text('Play Game', font, white, screen, 50, 75)
        draw_text('Options', font, white, screen, 50, 175)

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


# Options menu
def options():
    running = True
    x = 300
    x_btn = 425
    global minimumMoves
    global user_choice
    while running:
        # Load Background Image
        background = pygame.image.load('assets/menu.jpg')
        screen.blit(background, (0, 0))
        draw_text('Options', font, white, screen, 20, 20)
        draw_text('Choose the number of plates you want', font, white, screen, 150, 100)
        draw_text('Press ESC to exit', font, white, screen, 20, 565)
        draw_text('3 Disks - ', font, white, screen, x, 200)
        draw_text('4 Disks - ', font, white, screen, x, 300)
        draw_text('5 Disks - ', font, white, screen, x, 400)
        draw_text('Help - ', font, white, screen, x, 500)
        click = False
        # Button to generate the number of plates
        mark_x, mark_y = pygame.mouse.get_pos()

        button_1 = pygame.Rect(x_btn, 200, 25, 25)
        button_2 = pygame.Rect(x_btn, 300, 25, 25)
        button_3 = pygame.Rect(x_btn, 400, 25, 25)
        help_btn = pygame.Rect(x_btn, 500, 25, 25)
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
                    draw_text('You chose 3 disks', font, white, screen, x - 25, 450)
                    number_of_plates = 3
                    minimumMoves = min_moves(number_of_plates)
                    print('in options loop: ')
                    print(minimumMoves)
                    # Return 3
            if button_2.collidepoint((mark_x, mark_y)):
                if click:
                    draw_text('You chose 4 disks', font, white, screen, x - 25, 450)
                    number_of_plates = 4
                    minimumMoves = min_moves(number_of_plates)
                    print('in options loop: ')
                    print(minimumMoves)
                    # Return 4
            if button_3.collidepoint((mark_x, mark_y)):
                if click:
                    draw_text('You chose 5 disks', font, white, screen, x - 25, 450)
                    number_of_plates = 5
                    minimumMoves = min_moves(number_of_plates)
                    print('in options loop: ')
                    print(minimumMoves)
                    # Return 5
            if help_btn.collidepoint((mark_x, mark_y)):
                if click:
                    print('Success!')
                    help_menu()

        pygame.draw.rect(screen, white, button_1)
        pygame.draw.rect(screen, white, button_2)
        pygame.draw.rect(screen, white, button_3)
        pygame.draw.rect(screen, white, help_btn)
        pygame.display.update()
        mainClock.tick(60)


stick1_Location = (30, 75)
stick2_Location = (330, 75)
stick3_Location = (630, 75)


# Main game loop
def game():
    running = True
    global pauseQuit
    while running:
        # Load Background Image
        background = pygame.image.load('assets/background (1).png')
        screen.blit(background, (0, 0))
        # Load Stick Images onto screen
        stick = pygame.image.load('assets/Stick_Object_1.png')
        screen.blit(background, (0, 0))
        screen.blit(stick, stick1_Location)
        screen.blit(stick, stick2_Location)
        screen.blit(stick, stick3_Location)
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        pygame.draw.rect(screen, white, rectangle)
        pygame.draw.rect(screen, white, rectangle2)
        pygame.draw.rect(screen, white, rectangle3)
        # Draw text
        draw_text('Game', font, white, screen, 20, 20)
        draw_text('Minimum number of moves: ', font, white, screen, 350, 20)
        draw_text(str(minimumMoves), font, white, screen, 735, 20)
        draw_text('Moves: ', font, white, screen, 625, 60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                #if event.key == K_ESCAPE:
                    #running = False
                if event.key == K_p:
                    pause()
            if pauseQuit:
                running = False
                pauseQuit = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rectangle.collidepoint(event.pos):
                        rectangle_draging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rectangle.x - mouse_x
                        offset_y = rectangle.y - mouse_y
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rectangle_draging = False
            if event.type == pygame.MOUSEMOTION:
                if rectangle_draging:
                    mouse_x, mouse_y = event.pos
                    rectangle.x = mouse_x + offset_x
                    rectangle.y = mouse_y + offset_y
        pygame.display.update()
        mainClock.tick(60)


# Pause menu screen
def pause():
    paused = True
    global pauseQuit

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                if event.key == pygame.K_ESCAPE:
                    pauseQuit = True
                    paused = False

        draw_text('Paused', font, black, screen, 315, 50)

        draw_text('- Press C to continue.', font, black, screen, 250, 115)
        draw_text('- Press ESC to exit.', font, black, screen, 250, 145)

        pygame.display.update()
        mainClock.tick(5)


# Help Menu
def help_menu():
    running = True
    while running:
        background = pygame.image.load('assets/help.jpg')

        screen.blit(background, (0, 0))
        draw_text('Help Menu', font, white, screen, 20, 20)
        draw_text('Press ESC to exit', font, white, screen, 20, 565)
        draw_text('Designer: Édouard Lucas, 1883', font, white, screen, 20, 100)
        draw_text('This is a math puzzle', font, white, screen, 20, 200)
        draw_text('It starts with the disks in a neat stack in ascending order', font, white, screen, 20, 300)
        draw_text('Move the entire stack to another rod with least moves', font, white, screen, 20, 400)
        draw_text('Made by Shyamal Singh and Phillip Le', font, white, screen, 275, 565)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.key == K_ESCAPE:
                    running = False
        pygame.display.update()


# Generates 3 plates onto rod 1
def generate_3plates():
    #plate1 = pygame.image.load('assets/3Plates/Top.png')
    #plate2 = pygame.image.load('assets/3Plates/Middle.png')
    #plate3 = pygame.image.load('assets/3Plates/Bottom.png')
    two = 3
    #screen.blit(plate1, (58, 425))
    #screen.blit(plate2, (28, 445))
    #screen.blit(plate3, (18, 465))

    #pygame.display.update()


main_menu()
