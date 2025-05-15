import pygame
import random
import time
import os

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 36
TIME_LIMIT = 10  # seconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (160, 160, 160)
DARK_GRAY = (100, 100, 100)
BLUE = (50, 50, 255)

def load_words(filename):
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_random_phrase(words, word_count=6):
    return ' '.join(random.choices(words, k=word_count))

def calculate_wpm(input_text, start_time):
    if not start_time:
        return 0
    elapsed_time = time.time() - start_time
    word_count = len(input_text) / 5
    return (word_count / elapsed_time) * 60 if elapsed_time > 0 else 0

def render_colored_text(surface, font, target, input_text, x, y):
    for i, char in enumerate(target):
        if i < len(input_text):
            color = BLACK if input_text[i] == char else (255, 0, 0)  # Red if mistyped
        elif i == len(input_text):
            color = BLUE  # Cursor position
        else:
            color = GRAY
        ch_surf = font.render(char, True, color)
        surface.blit(ch_surf, (x, y))
        x += ch_surf.get_width()

def start_typing_game(screen):
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
    running = True

    back_button = pygame.Rect(10, 10, 100, 40)
    back_text = button_font.render("Back", True, BLACK)

    while running:
        screen.fill(WHITE)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_x, mouse_y):
                    return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    pass  # Ignore Enter key
                elif event.key == pygame.K_SPACE:
                    # Only allow progressing if the line is fully and correctly typed
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

                # Check if line is typed correctly (but wait for space to move on)
                if input_text.strip() == target_lines[current_line_index]:
                    line_complete = True

        # Render target lines
        line_y = HEIGHT // 3
        for idx, line in enumerate(target_lines):
            if idx == current_line_index:
                render_colored_text(screen, font, line, input_text, 50, line_y)
            else:
                line_surface = font.render(line, True, GRAY)
                screen.blit(line_surface, (50, line_y))
            line_y += FONT_SIZE + 15

        # Render timer & WPM
        if start_time:
            elapsed = time.time() - start_time
            remaining = max(0, TIME_LIMIT - elapsed)

            # Update WPM once every second
            current_time = time.time()
            if current_time - last_wpm_update >= 1:
                wpm = calculate_wpm(input_text, start_time)
                last_wpm_update = current_time
        else:
            remaining = TIME_LIMIT
            wpm = 0

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

    pygame.quit()
