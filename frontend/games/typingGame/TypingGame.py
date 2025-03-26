import pygame
import random
import time
import os

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 48
TEXT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
TIME_LIMIT = 30  # Total time limit in seconds

class TypingGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Typing Test Clone")
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.words = self.load_words('words.txt')
        self.running = True
        self.input_text = ""
        self.target_phrase = self.get_random_phrase()
        self.start_time = None
        self.wpm = 0

    def load_words(self, filename):
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]

    def get_random_phrase(self, word_count=5):
        return ' '.join(random.choices(self.words, k=word_count))

    def calculate_wpm(self):
        if self.start_time is None:
            return 0
        elapsed_time = time.time() - self.start_time
        if elapsed_time > 0:
            characters_typed = len(self.input_text)
            words_typed = characters_typed / 5  # Average word length is 5 chars
            return (words_typed / elapsed_time) * 60
        return 0

    def start_typing_game(self):
        clock = pygame.time.Clock()
        while self.running:
            self.screen.fill(BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.input_text == self.target_phrase:
                            self.input_text = ""
                            self.target_phrase = self.get_random_phrase()
                            self.start_time = None  # Reset timer
                        else:
                            self.input_text = ""  # Reset input on wrong attempt
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        self.input_text += event.unicode
                        if self.start_time is None:
                            self.start_time = time.time()

            # Calculate remaining time
            if self.start_time is not None:
                elapsed_time = time.time() - self.start_time
                remaining_time = max(0, TIME_LIMIT - elapsed_time)
                self.wpm = self.calculate_wpm()
            else:
                remaining_time = TIME_LIMIT  # Timer not started yet
                self.wpm = 0

            # Render the target phrase and user input
            target_surface = self.font.render(self.target_phrase, True, TEXT_COLOR)
            input_surface = self.font.render(self.input_text, True, TEXT_COLOR)

            self.screen.blit(target_surface, (50, HEIGHT // 2 - FONT_SIZE))
            self.screen.blit(input_surface, (50, HEIGHT // 2 + FONT_SIZE))

            # Render the countdown timer
            timer_surface = self.font.render(f'Time: {int(remaining_time)}', True, TEXT_COLOR)
            self.screen.blit(timer_surface, (WIDTH - 200, 50))

            # Check if time is up
            if remaining_time <= 0:
                self.input_text = ""  # Reset input
                self.target_phrase = self.get_random_phrase()  # Get a new phrase
                self.start_time = None  # Reset the timer

            # Display the WPM
            wpm_surface = self.font.render(f'WPM: {int(self.wpm)}', True, TEXT_COLOR)
            self.screen.blit(wpm_surface, (WIDTH - 200, 100))

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = TypingGame()
    game.start_typing_game()
