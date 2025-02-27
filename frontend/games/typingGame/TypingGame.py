import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 48
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
TIME_LIMIT = 30  # Total time limit in seconds

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Test Clone")
font = pygame.font.Font(None, FONT_SIZE)

# Function that loads a file 
def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Load the words from words.txt
words = load_words('words.txt')

# Function to get a random phrase
def get_random_phrase(word_count=5):
    return ' '.join(random.choices(words, k=word_count))

def main():
    running = True
    input_text = ""
    target_phrase = get_random_phrase()
    start_time = None
    score = 0

    while running:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == target_phrase:
                        score += 1
                        input_text = ""
                        target_phrase = get_random_phrase()
                        start_time = None  # Reset timer
                    else:
                        input_text = ""  # Reset input on wrong attempt
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
                    if start_time is None:  # Start timer on first input
                        start_time = time.time()

        # Calculate remaining time
        if start_time is not None:
            elapsed_time = time.time() - start_time
            remaining_time = max(0, TIME_LIMIT - elapsed_time)
        else:
            remaining_time = TIME_LIMIT  # Timer not started yet

        # Render the target phrase and user input
        target_surface = font.render(target_phrase, True, TEXT_COLOR)
        input_surface = font.render(input_text, True, TEXT_COLOR)

        screen.blit(target_surface, (50, HEIGHT // 2 - FONT_SIZE))
        screen.blit(input_surface, (50, HEIGHT // 2 + FONT_SIZE))

        # Render the countdown timer
        timer_surface = font.render(f'Time: {remaining_time:.2f}', True, TEXT_COLOR)
        screen.blit(timer_surface, (WIDTH - 200, 50))

        # Check if time is up
        if remaining_time <= 0:
            input_text = ""  # Reset input
            target_phrase = get_random_phrase()  # Get a new phrase
            start_time = None  # Reset the timer

        # Display the score
        score_surface = font.render(f'Score: {score}', True, TEXT_COLOR)
        screen.blit(score_surface, (WIDTH - 200, 100))

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
