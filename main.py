import pygame
import sys
import os
from frontend.games.ReactionTimeGame import ReactionTime  # Import the Reaction Time game logic

# Determine the base path for accessing files in the bundled app or during development
if getattr(sys, 'frozen', False):  # Check if running as a bundled executable
    base_path = sys._MEIPASS
else:
    base_path = os.getcwd()

pygame.init()

# Screen configuration
res = (720, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Main Menu")

# Colors
white = (255, 255, 255)
gray = (200, 200, 200)
dark_gray = (100, 100, 100)
black = (0, 0, 0)

button_color = gray
button_hover_color = dark_gray
button_position = (250, 325)
button_size = (200, 60)

font = pygame.font.Font(None, 36)
button_text = font.render("Reaction Time", True, black)

running = True
while running:
    screen.fill(white)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Define button area and hover logic
    button_rect = pygame.Rect(button_position, button_size)
    if button_rect.collidepoint(mouse_x, mouse_y):
        color = button_hover_color
    else:
        color = button_color

    pygame.draw.rect(screen, color, button_rect)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_x, mouse_y):
                # Run the Reaction Time game using the existing screen
                ReactionTime.start_reaction_time_game(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
