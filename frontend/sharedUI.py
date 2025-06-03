import pygame

# Initialize pygame fonts globally to reuse
pygame.font.init()

# Colors
white = (255, 255, 255)
gray = (200, 200, 200)
dark_gray = (100, 100, 100)
black = (0, 0, 0)

# Fonts
LABEL_FONT = pygame.font.Font(None, 28)
INPUT_FONT = pygame.font.Font(None, 36)
BUTTON_FONT = pygame.font.Font(None, 36)

def draw_label(screen, text, position, font=LABEL_FONT, color=black):
    """
    Draws a label (text) on the screen.
    
    Args:
        screen (pygame.Surface): The screen to draw on.
        text (str): The text to display.
        position (tuple): (x, y) position of the label.
        font (pygame.Font): The font to use for the label.
        color (tuple): The color of the label.
    """
    label_surface = font.render(text, True, color)
    screen.blit(label_surface, position)

def draw_input_box(screen, box, active_color=dark_gray, inactive_color=gray):
    """
    Draws an input box on the screen.
    
    Args:
        screen (pygame.Surface): The screen to draw on.
        box (dict): A dictionary containing input box properties: 
                    - "rect" (pygame.Rect): The box rectangle.
                    - "text" (str): The text inside the box.
                    - "active" (bool): Whether the box is active.
        active_color (tuple): Color when the box is active.
        inactive_color (tuple): Color when the box is inactive.
    """
    color = active_color if box["active"] else inactive_color
    pygame.draw.rect(screen, color, box["rect"])
    pygame.draw.rect(screen, black, box["rect"], 2)
    
    # Mask the text if it's a password box
    display_text = box["text"] if not box.get("password") else "*" * len(box["text"])
    text_surface = INPUT_FONT.render(display_text, True, black)
    screen.blit(text_surface, (box["rect"].x + 5, box["rect"].y + 5))

def handle_input_event(event, input_boxes):
    """
    Handles user input for active input boxes.
    
    Args:
        event (pygame.event.Event): The event to handle.
        input_boxes (list): A list of input box dictionaries.
    """
    pygame.key.set_repeat(300, 50)  # Enable key repeat (300ms delay, then 50ms interval)
    
    for box in input_boxes:
        if box["active"]:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    box["text"] = box["text"][:-1]  
                elif event.key == pygame.K_RETURN:
                    box["active"] = False  
                else:
                    box["text"] += event.unicode


    
"""     for box in input_boxes:
        if box["active"]:
            if event.key == pygame.K_BACKSPACE:
                box["text"] = box["text"][:-1]
            else:l
                box["text"] += event.unicode """


def draw_button(screen, rect, text, font=BUTTON_FONT, color=gray, hover_color=dark_gray, text_color=black):
    """
    Draws a button with hover effect and returns whether it's clicked.
    
    Args:
        screen (pygame.Surface): The screen to draw on.
        rect (pygame.Rect): The rectangle for the button.
        text (str): The text on the button.
        font (pygame.Font): The font of the button text.
        color (tuple): The default color of the button.
        hover_color (tuple): The color when the button is hovered.
        text_color (tuple): The color of the button text.
    
    Returns:
        bool: True if the button is clicked, False otherwise.
    """
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    current_color = hover_color if rect.collidepoint(mouse_pos) else color
    pygame.draw.rect(screen, current_color, rect)
    pygame.draw.rect(screen, black, rect, 2)

    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

    return rect.collidepoint(mouse_pos) and mouse_click[0]  # Return True if clicked