import pygame
import sys
import subprocess
import os

pygame.init()

res = (720, 720)

screen = pygame.display.set_mode(res)
pygame.display.set_caption("Main Menu")

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


    mouse_x, mouse_y = pygame.mouse.get_pos()

    button_rect = pygame.Rect(button_position, button_size)
    if button_rect.collidepoint(mouse_x, mouse_y):
        color = button_hover_color
    else :
        color = button_color


    pygame.draw.rect(screen, color, button_rect)
    text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(mouse_x, mouse_y):
                game_path = os.path.join(os.getcwd(),"frontend", "games", "ReactionTime.py")
                try:
                    subprocess.run(["python", game_path])
                except FileNotFoundError:
                    print(f"Error: The file {game_path} was not found")
    
    pygame.display.flip()

pygame.quit()
sys.exit()