import pygame
import random
import time
import os
from backend.databaseConnection import save_wpm_score

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 36
TIME_LIMIT = 5  # seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
DARK_GRAY = (100, 100, 100)
BLUE = (50, 50, 255)
RED = (255, 0, 0)

def load_words(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_phrase(words, word_count=6):
    return ' '.join(random.choices(words, k=word_count))

def calculate_wpm(correct_char_count, start_time):
    if not start_time:
        return 0
    elapsed_time = time.time() - start_time
    word_count = correct_char_count / 5
    return (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0

def render_colored_text(surface, font, target, input_text, x, y):
    for i, char in enumerate(target):
        if i < len(input_text):
            color = BLACK if input_text[i] == char else RED
        elif i == len(input_text):
            color = BLUE  # Cursor indicator
        else:
            color = GRAY
        ch_surf = font.render(char, True, color)
        surface.blit(ch_surf, (x, y))
        x += ch_surf.get_width()

def show_results_screen(screen, final_wpm):
    screen.fill(WHITE)
    font = pygame.font.SysFont(None, 48)
    message = font.render(f"Time's up! Final WPM: {int(final_wpm)}", True, BLACK)
    message_rect = message.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(message, message_rect)
    pygame.display.flip()
    pygame.time.delay(3000)

def start_typing_game(screen, user_id=1):
    pygame.display.set_caption("Typing Test Clone")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE)
    button_font = pygame.font.SysFont(None, 32)

    words = load_words('words.txt')
    input_text = ""
    current_line_index = 0
    target_lines = [get_random_phrase(words) for _ in range(3)]
    line_complete = False

    start_time = None
    last_wpm_update = 0
    wpm = 0
<<<<<<< HEAD
    timer_expired = False
    end_screen_shown = False
=======
    running = True
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1

    back_button = pygame.Rect(10, 10, 100, 40)
    back_text = button_font.render("Back", True, BLACK)

<<<<<<< HEAD
    while True:
=======
    while running:
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1
        screen.fill(WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
<<<<<<< HEAD
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_x, mouse_y):
                    return
            elif event.type == pygame.KEYDOWN and not timer_expired:
=======
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_x, mouse_y):
                    return
            elif event.type == pygame.KEYDOWN:
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass
                elif event.key == pygame.K_SPACE:
                    if input_text.strip() == target_lines[current_line_index]:
                        current_line_index += 1
                        input_text = ""
                        line_complete = False
                        target_lines.append(get_random_phrase(words))
                    else:
                        input_text += " "
                else:
                    input_text += event.unicode
                    if not start_time:
                        start_time = time.time()
                        last_wpm_update = start_time

                if input_text.strip() == target_lines[current_line_index]:
                    line_complete = True

        # Live correct character count
        current_target = target_lines[current_line_index]
        correct_chars = sum(1 for i in range(min(len(input_text), len(current_target)))
                            if input_text[i] == current_target[i])
        total_correct_chars = correct_chars

<<<<<<< HEAD
        # Timer and WPM update
=======
        # Timer
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1
        if start_time:
            elapsed = time.time() - start_time
            remaining = max(0, TIME_LIMIT - elapsed)

<<<<<<< HEAD
            if remaining <= 0 and not timer_expired:
                final_wpm = calculate_wpm(total_correct_chars, start_time)
                save_wpm_score(user_id, final_wpm)
                show_results_screen(screen, final_wpm)
                timer_expired = True
                wpm = final_wpm  # keep final wpm here
                remaining = 0  # Keep timer frozen
            elif not timer_expired and time.time() - last_wpm_update >= 1:
                wpm = calculate_wpm(total_correct_chars, start_time)
                last_wpm_update = time.time()
            elif timer_expired:
                # After timer expired, keep wpm frozen at final_wpm
                wpm = final_wpm
=======
            # Update WPM only once per second
            if time.time() - last_wpm_update >= 1:
                wpm = calculate_wpm(total_correct_chars, start_time)
                last_wpm_update = time.time()
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1
        else:
            remaining = TIME_LIMIT
            wpm = 0

<<<<<<< HEAD
=======
        # Time’s up check
        if remaining <= 0 and start_time is not None:
            final_wpm = calculate_wpm(total_correct_chars, start_time)
            show_results_screen(screen, final_wpm)
            save_wpm_score(user_id, final_wpm)
            start_time = None  # Stop the timer

>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1

        # Render lines
        line_y = HEIGHT // 3
        for idx, line in enumerate(target_lines):
            if idx == current_line_index:
                render_colored_text(screen, font, line, input_text, 50, line_y)
            else:
                line_surface = font.render(line, True, GRAY)
                screen.blit(line_surface, (50, line_y))
            line_y += FONT_SIZE + 15

        # Timer and WPM
        timer = font.render(f"Time: {int(remaining)}", True, BLACK)
        wpm_display = font.render(f"WPM: {int(wpm)}", True, BLACK)
        screen.blit(timer, (WIDTH - 200, 40))
        screen.blit(wpm_display, (WIDTH - 200, 80))

        # Back button
        button_color = DARK_GRAY if back_button.collidepoint(mouse_x, mouse_y) else GRAY
        pygame.draw.rect(screen, button_color, back_button)
        back_text_rect = back_text.get_rect(center=back_button.center)
        screen.blit(back_text, back_text_rect)

        pygame.display.flip()
        clock.tick(FPS)

<<<<<<< HEAD
    pygame.quit()
=======
    pygame.quit()
>>>>>>> 11c438d2abe29c4b71eea8f85950349a10371db1
