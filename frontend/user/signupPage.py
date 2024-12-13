import pygame
import sys
from backend.databaseConnection import register_user
from frontend.sharedUI import draw_label, draw_input_box, draw_button, handle_input_event

def signup_page(screen):
    pygame.init()

    # Colors
    white = (255, 255, 255)

    # Input boxes
    input_boxes = [
        {"label": "Name:", "rect": pygame.Rect(260, 150, 200, 40), "text": "", "active": False},
        {"label": "Email:", "rect": pygame.Rect(260, 220, 200, 40), "text": "", "active": False},
        {"label": "Password:", "rect": pygame.Rect(260, 290, 200, 40), "text": "", "active": False, "password": True},
        {"label": "Phone:", "rect": pygame.Rect(260, 360, 200, 40), "text": "", "active": False},
    ]

    # Buttons
    register_button_rect = pygame.Rect(260, 430, 200, 50)
    back_button_rect = pygame.Rect(10, 10, 120, 50)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Activate input boxes
                for box in input_boxes:
                    box["active"] = box["rect"].collidepoint(event.pos)

                # Check button clicks
                if draw_button(screen, back_button_rect, "Back"):
                    return  # Go back to the login page

                elif draw_button(screen, register_button_rect, "Register"):
                    # Extract input data
                    name = input_boxes[0]["text"]
                    email = input_boxes[1]["text"]
                    password = input_boxes[2]["text"]
                    phone = input_boxes[3]["text"]

                    # Register the user
                    try:
                        register_user(name, password, email, phone)
                        print("Registration successful!")
                    except Exception as e:
                        print(f"Registration failed: {e}")

            elif event.type == pygame.KEYDOWN:
                # Handle input for active input boxes
                handle_input_event(event, input_boxes)

        # Draw screen
        screen.fill(white)

        # Draw input boxes and labels
        for box in input_boxes:
            draw_label(screen, box["label"], (box["rect"].x, box["rect"].y - 30))
            draw_input_box(screen, box)

        # Draw buttons
        draw_button(screen, register_button_rect, "Register")
        draw_button(screen, back_button_rect, "Back")

        pygame.display.flip()
