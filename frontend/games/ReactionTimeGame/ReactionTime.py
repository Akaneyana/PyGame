import pygame
import time
import random
from backend.databaseConnection import save_reaction_time  # Import the function to save the score

# Colors
white = (255, 255, 255)
gray = (200, 200, 200)
dark_gray = (100, 100, 100)
black = (0, 0, 0)
red = (255, 4, 4)
yellow = (255, 252, 4)
green = (8, 252, 4)

# Frame rate
clock = pygame.time.Clock()
FPS = 60

def start_reaction_time_game(screen, user_id):
    """Run the Reaction Time game on the provided Pygame screen."""
    # Get screen dimensions
    screen_width, screen_height = screen.get_size()

    # Font and text setup
    main_font = pygame.font.SysFont(None, 90)
    button_font = pygame.font.Font(None, 36)

    # Text elements
    title = main_font.render("Reaction Time Test", True, red)
    title_rect = title.get_rect(center=(screen_width // 2, screen_height // 8))

    click_to_start = main_font.render("Click to Start", True, black)
    click_to_start_rect = click_to_start.get_rect(center=(screen_width // 2, screen_height // 2))

    waiting = main_font.render("Wait...", True, black)
    waiting_rect = waiting.get_rect(center=(screen_width // 2, screen_height // 2))

    click = main_font.render("Click NOW!", True, black)
    click_rect = click.get_rect(center=(screen_width // 2, screen_height // 2))

    early = main_font.render("Clicked Too Early", True, black)
    early_rect = early.get_rect(center=(screen_width // 2, screen_height // 2))

    # Back button setup
    button_size = (120, 50)
    button_position = (10, 10)
    back_button_rect = pygame.Rect(button_position, button_size)
    back_button_text = button_font.render("Back", True, black)

    game_state = "Click to Start"
    start_time, end_time = 0, 0
    waiting_start_time = 0
    delay_time = 0
    reaction_time = None
    score_saved = False  # Flag to track whether the score has been saved

    running = True
    while running:
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Button color and hover logic
        button_color = gray
        if back_button_rect.collidepoint(mouse_x, mouse_y):
            button_color = dark_gray

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()  # Ensure the program closes completely
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(mouse_x, mouse_y):
                    return  # Exit to the main menu
                if game_state == "Click to Start":
                    game_state = "Waiting"
                    waiting_start_time = time.time()
                    delay_time = random.uniform(2, 5)  # Set a random delay for the test
                elif game_state == "Waiting":
                    game_state = "Too Early"
                elif game_state == "Test Starting":
                    end_time = time.time()
                    game_state = "Showing Results"
                elif game_state == "Too Early" or game_state == "Showing Results":
                    game_state = "Click to Start"
                    score_saved = False  # Reset the score flag for a new game

        # Screen background
        screen.fill(white)

        # Draw back button
        pygame.draw.rect(screen, button_color, back_button_rect)
        text_rect = back_button_text.get_rect(center=back_button_rect.center)
        screen.blit(back_button_text, text_rect)

        # Draw game content
        screen.blit(title, title_rect)

        if game_state == "Click to Start":
            screen.blit(click_to_start, click_to_start_rect)
        elif game_state == "Waiting":
            screen.fill(yellow)
            screen.blit(waiting, waiting_rect)

            # Transition to "Test Starting" after the delay
            if time.time() - waiting_start_time >= delay_time:
                game_state = "Test Starting"
                start_time = time.time()
        elif game_state == "Test Starting":
            screen.fill(green)
            screen.blit(click, click_rect)
        elif game_state == "Too Early":
            screen.fill(red)
            screen.blit(early, early_rect)
        elif game_state == "Showing Results":
            reaction_time = round((end_time - start_time) * 1000)  # Reaction time in milliseconds
            score_text = main_font.render(f"Speed: {reaction_time} ms", True, black)
            screen.blit(score_text, click_to_start_rect)

            if not score_saved:  # Save the score only once
                save_reaction_time(user_id, reaction_time)  # Save reaction time for the logged-in user
                score_saved = True  # Set the flag after saving

        pygame.display.update()

        # caps the frame rate at the FPS value which is 60
        clock.tick(FPS)
