import pygame
import sys
from frontend.user.signupPage import signup_page
from backend.databaseConnection import verify_user_credentials, update_last_logged_in
from frontend.sharedUI import draw_label, draw_input_box, draw_button, handle_input_event

# Default user ID if no login occurs
DEFAULT_USER_ID = 1

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
    signup_button_rect = pygame.Rect(260, 360, 200, 50)
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
                    return DEFAULT_USER_ID  # Return default user ID when going back
                elif draw_button(screen, login_button_rect, "Login"):
                    email = input_boxes[0]["text"]
                    password = input_boxes[1]["text"]
                    
                    try:
                        user_id = verify_user_credentials(email, password)
                        if user_id:
                            print(f"Login successful! Welcome User {user_id}")
                            update_last_logged_in(user_id)
                            return user_id  # Return logged-in user ID
                        else:
                            print("Invalid credentials.")
                    except Exception as e:
                        print(f"Login failed: {e}")
                elif draw_button(screen, signup_button_rect, "Go to Signup"):
                    signup_page(screen)
            elif event.type == pygame.KEYDOWN:
                handle_input_event(event, input_boxes)

        # Draw screen
        screen.fill(white)

        for box in input_boxes:
            draw_label(screen, box["label"], (box["rect"].x, box["rect"].y - 30))
            draw_input_box(screen, box)

        draw_button(screen, login_button_rect, "Login")
        draw_button(screen, back_button_rect, "Back")
        draw_button(screen, signup_button_rect, "Go to Signup")

        pygame.display.flip()
