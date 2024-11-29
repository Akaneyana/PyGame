import pygame
import sys
import time
import random

# Start using pygame
pygame.init()

# Screen dimensions
res = (720, 720)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Reaction Time")

# Font and text setup
main_font = pygame.font.SysFont(None, 90)

title = main_font.render("Reaction Time Test", True, "red")
title_rect = title.get_rect(center=(360, 50))

click_to_start = main_font.render("Click to Start", True, "black")
click_to_start_rect = click_to_start.get_rect(center=(360, 360))

waiting = main_font.render("Wait...", True, "black")
waiting_rect = waiting.get_rect(center=(360, 360))

click = main_font.render("Click NOW!", True, "black")
click_rect = click.get_rect(center=(360, 360))

early = main_font.render("Clicked Too Early", True, "black")
early_rect = early.get_rect(center=(360, 360))

score = main_font.render("Score: 1000 ms", True, "red")
score_rect = score.get_rect(center=(360, 360))

game_state = "Click to Start"

start_time, end_time = 0, 0
waiting_start_time = 0
delay_time = 0

# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_state == "Click to Start":
                game_state = "Waiting"
                waiting_start_time = time.time()  # Record the time when waiting starts
                delay_time = random.uniform(2, 15)  # Set a random delay for the test to start
            elif game_state == "Waiting":
                # Transition to "Too Early" state if clicked during "Waiting"
                game_state = "Too Early"
            elif game_state == "Test Starting":
                end_time = time.time()
                game_state = "Showing Results"
            elif game_state == "Too Early":
                game_state = "Click to Start"
            elif game_state == "Showing Results":
                game_state = "Click to Start"

    screen.fill("white")

    screen.blit(title, title_rect)

    if game_state == "Click to Start":
        screen.blit(click_to_start, click_to_start_rect)
    elif game_state == "Waiting":
        screen.fill("yellow")
        screen.blit(waiting, waiting_rect)

        # Transition to "Test Starting" after the delay
        if time.time() - waiting_start_time >= delay_time:
            game_state = "Test Starting"
            start_time = time.time()  # Record the time when the test starts
    elif game_state == "Test Starting":
        screen.fill("green")
        screen.blit(click, click_rect)
    elif game_state == "Too Early":
        screen.fill("red")
        screen.blit(early, early_rect)
    elif game_state == "Showing Results":
        reaction_time = round((end_time - start_time) * 1000)
        score_text = main_font.render(f"Speed: {reaction_time} ms", True, "black")
        screen.blit(score_text, score_rect)

    pygame.display.update()
