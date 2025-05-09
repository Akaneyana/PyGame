import pygame
import sys
import os
from frontend.games.reactionTimeGame import reactionTime  # Import the Reaction Time game logic
from frontend.user.loginPage import login_page  # Import the login page function

# Determine the base path for accessing files in the bundled app or during development
if getattr(sys, 'frozen', False):  # Check if running as a bundled executable
    base_path = sys._MEIPASS
else:
    base_path = os.getcwd()
pygame.init()

# Screen configuration
res = (720, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("")

# Colors
white = (255, 255, 255)
gray = (200, 200, 200)
dark_gray = (100, 100, 100)
black = (0, 0, 0)

button_color = gray
button_hover_color = dark_gray
button_size = (175, 50)
game_button_size = (200, 60)

font = pygame.font.Font(None, 36)
reaction_time_text = font.render("Reaction Time", True, black)
login_page_text = font.render("Login Page", True, black)

# Button positions
reaction_time_button_position = (250, 300)
login_page_button_position = (525, 30)

# Frame Rate
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    screen.fill(white)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Reaction Time button
    reaction_time_button_rect = pygame.Rect(reaction_time_button_position, game_button_size)
    reaction_time_color = button_hover_color if reaction_time_button_rect.collidepoint(mouse_x, mouse_y) else button_color
    pygame.draw.rect(screen, reaction_time_color, reaction_time_button_rect)
    reaction_time_text_rect = reaction_time_text.get_rect(center=reaction_time_button_rect.center)
    screen.blit(reaction_time_text, reaction_time_text_rect)

    # Login Page button
    login_page_button_rect = pygame.Rect(login_page_button_position, button_size)
    login_page_color = button_hover_color if login_page_button_rect.collidepoint(mouse_x, mouse_y) else button_color
    pygame.draw.rect(screen, login_page_color, login_page_button_rect)
    login_page_text_rect = login_page_text.get_rect(center=login_page_button_rect.center)
    screen.blit(login_page_text, login_page_text_rect)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reaction_time_button_rect.collidepoint(mouse_x, mouse_y):
                reactionTime.start_reaction_time_game(screen, 1)  # Navigate to Reaction Time game
            elif login_page_button_rect.collidepoint(mouse_x, mouse_y):
                login_page(screen)  # Navigate to Login Page

    pygame.display.flip()
    
    # caps the frame rate at the FPS value which is 60
    clock.tick(FPS)

pygame.quit()
sys.exit()
