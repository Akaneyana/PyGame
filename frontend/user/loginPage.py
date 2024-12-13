import pygame
import sys
from frontend.user.signupPage import signup_page  # Import the signup page function
from backend.databaseConnection import verify_user_credentials  # Import the new function for login check
from frontend.sharedUI import draw_label, draw_input_box, draw_button, handle_input_event

def login_page(screen):
    pygame.init()

    # Colors
    white = (255, 255, 255)

    # Input boxes
    input_boxes = [
        {"label": "Email:", "rect": pygame.Rect(260, 150, 200, 40), "text": "", "active": False},
        {"label": "Password:", "rect": pygame.Rect(260, 220, 200, 40), "text": "", "active": False, "password": True},
    ]

    # Buttons
    login_button_rect = pygame.Rect(260, 290, 200, 50)
    signup_button_rect = pygame.Rect(260, 360, 200, 50)  # Button to go to signup page
    back_button_rect = pygame.Rect(10, 10, 120, 50)  # Button to go back to main menu

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
                if draw_button(screen, back_button_rect, "Back to Main Menu"):
                    return  # Exit to the main menu
                elif draw_button(screen, login_button_rect, "Login"):
                    # Extract input data
                    email = input_boxes[0]["text"]
                    password = input_boxes[1]["text"]
                    # Attempt to login with the provided credentials
                    try:
                        if verify_user_credentials(email, password):
                            print("Login successful!")
                            # Proceed to the next page or action
                        else:
                            print("Invalid credentials.")
                    except Exception as e:
                        print(f"Login failed: {e}")
                elif draw_button(screen, signup_button_rect, "Go to Signup"):
                    signup_page(screen)  # Navigate to Signup Page
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
        draw_button(screen, login_button_rect, "Login")
        draw_button(screen, back_button_rect, "Back to Main Menu")
        draw_button(screen, signup_button_rect, "Go to Signup")

        pygame.display.flip()
