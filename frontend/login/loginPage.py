import pygame
import bcrypt
from backend.databaseConnection import register_user

def hash_password(password):
    """Hash the password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def login_page(screen):
    """
    Function to display the login/registration page and handle user input.
    The password will be hashed before saving into the database.
    """
    font = pygame.font.Font(None, 36)

    # Input box configuration
    input_box_width = 200
    input_box_height = 40
    input_boxes = {
        'name': pygame.Rect(250, 100, input_box_width, input_box_height),
        'email': pygame.Rect(250, 150, input_box_width, input_box_height),
        'password': pygame.Rect(250, 200, input_box_width, input_box_height),
        'phone': pygame.Rect(250, 250, input_box_width, input_box_height)
    }

    # Placeholder texts
    input_texts = {
        'name': "",
        'email': "",
        'password': "",
        'phone': ""
    }

    # Input flags for active fields
    active_input = None

    # Submit button
    submit_button = pygame.Rect(250, 300, input_box_width, 60)
    submit_text = font.render("Submit", True, (0, 0, 0))

    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((255, 255, 255))  # White background

        # Draw input fields
        for field, rect in input_boxes.items():
            color = (200, 200, 200) if field != active_input else (180, 180, 255)
            pygame.draw.rect(screen, color, rect)
            text_surface = font.render(input_texts[field], True, (0, 0, 0))
            screen.blit(text_surface, (rect.x + 10, rect.y + 10))

        # Draw Submit button
        pygame.draw.rect(screen, (200, 200, 200), submit_button)
        screen.blit(submit_text, submit_button.center)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle field activation based on clicks
                for field, rect in input_boxes.items():
                    if rect.collidepoint(event.pos):
                        active_input = field
                        break
                if submit_button.collidepoint(event.pos):
                    # On submit, hash password and save data to DB
                    if all(input_texts.values()):
                        hashed_password = hash_password(input_texts['password'])
                        # Call the register_user function to save to the DB
                        register_user(input_texts['name'], input_texts['email'], hashed_password, input_texts['phone'])
                        print("User registered successfully!")
                        running = False  # Close the page after submission
                    else:
                        print("Please fill in all fields.")

            if event.type == pygame.KEYDOWN:
                if active_input:
                    if event.key == pygame.K_RETURN:
                        # Handle submission on Enter key
                        if all(input_texts.values()):
                            hashed_password = hash_password(input_texts['password'])
                            register_user(input_texts['name'], input_texts['email'], hashed_password, input_texts['phone'])
                            print("User registered successfully!")
                            running = False
                    elif event.key == pygame.K_BACKSPACE:
                        # Handle Backspace for deleting characters
                        input_texts[active_input] = input_texts[active_input][:-1]
                    else:
                        # Handle normal typing
                        input_texts[active_input] += event.unicode

        pygame.display.update()
        clock.tick(30)  # Limit to 30 frames per second

