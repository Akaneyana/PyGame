import pygame
import sys
import subprocess
import os

# Determine the base path for accessing files in the bundled app or during development
if getattr(sys, 'frozen', False):  # Check if running as a bundled executable
    base_path = sys._MEIPASS  # Temporary folder used by PyInstaller
else:  # Running as a script (during development)
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
                # Update the path to reactiontime.py, considering bundled environment
                game_path = os.path.join(base_path, "frontend", "games", "reactiontime.py")
                
                # Make sure the file exists before trying to run it
                if not os.path.exists(game_path):
                    print(f"Error: The file {game_path} was not found")
                else:
                    try:
                        # Run the game script using the correct Python interpreter
                        subprocess.run([sys.executable, game_path])
                    except Exception as e:
                        print(f"Failed to execute the script: {e}")

    pygame.display.flip()

pygame.quit()
sys.exit()
