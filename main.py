import pygame
import sys
import os
from frontend.games.reactionTimeGame.ReactionTime import start_reaction_time_game
from frontend.user.loginPage import login_page
from frontend.games.typingGame.TypingGame import start_typing_game


# Determine base path for resource access
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.getcwd()

pygame.init()

# Screen configuration
res = (720, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Game Selection")

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
typing_game_text = font.render("Typing Game", True, black)
login_page_text = font.render("Login Page", True, black)

# Button positions
reaction_time_button_position = (250, 150)
typing_game_button_position = (250, 250)
login_page_button_position = (525, 30)

# Frame Rate
clock = pygame.time.Clock()
FPS = 60

# Default user ID if not logged in
logged_in_user_id = 1  # Default to User_Id 1

running = True
while running:
    screen.fill(white)

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Reaction Time Game button
    reaction_time_button_rect = pygame.Rect(reaction_time_button_position, game_button_size)
    reaction_time_color = button_hover_color if reaction_time_button_rect.collidepoint(mouse_x, mouse_y) else button_color
    pygame.draw.rect(screen, reaction_time_color, reaction_time_button_rect)
    reaction_time_text_rect = reaction_time_text.get_rect(center=reaction_time_button_rect.center)
    screen.blit(reaction_time_text, reaction_time_text_rect)

    # Typing Game Button
    typing_game_button_rect = pygame.Rect(typing_game_button_position, game_button_size)
    typing_game_color = button_hover_color if typing_game_button_rect.collidepoint(mouse_x, mouse_y) else button_color
    pygame.draw.rect(screen, typing_game_color, typing_game_button_rect)
    typing_game_text_rect = typing_game_text.get_rect(center=typing_game_button_rect.center)
    screen.blit(typing_game_text, typing_game_text_rect)

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
                start_reaction_time_game(screen, logged_in_user_id)
            elif typing_game_button_rect.collidepoint(mouse_x, mouse_y):
                start_typing_game(screen)
            elif login_page_button_rect.collidepoint(mouse_x, mouse_y):
                user_id = login_page(screen)
                if user_id:
                    logged_in_user_id = user_id  # Update logged-in user ID

    pygame.display.flip()
    
    clock.tick(FPS)

pygame.quit()
sys.exit()