import time
import pygame
from games_funcs import generate_paragraph, wrapline, get_key_character, shift_number_map

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FONT_SIZE = 20
LINE_HEIGHT = FONT_SIZE + 5

# Generate text for the game
text = generate_paragraph()

# Initialize fonts
my_font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

# Wrap the text
wrapped_text = wrapline(text, my_font, WINDOW_WIDTH - 20)

# Score
speed = 0

# Text rectangles and rendering
start_screen = my_font.render("START TYPE RACER", True, "white")
space = my_font.render("Press ANY KEY to Play", True, "white")
type_speed = my_font.render(f"Type Speed: {speed}", True, "white")

type_speed_rect = type_speed.get_rect(center=(500, 800))
start_screen_rect = start_screen.get_rect(center=(500, 100))
space_rect = space.get_rect(center=(500, 800))

# Pygame setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Type Racer')
clock = pygame.time.Clock()
running = True
shift_pressed = False
start = True
colour = {}
user_input = []
count = 0

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and start:
            start = False
            user_input = []
            count = 0
        elif not start:
            if event.type == pygame.KEYDOWN:
                # Have a list with what the user has typed
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift_pressed = True
                else:
                    key_name = pygame.key.name(event.key)
                    if key_name == "caps lock":
                        count += 1
                    elif key_name == "backspace":
                        if user_input:
                            user_input.pop()
                    elif key_name == "space":
                        user_input.append(" ")
                    else:
                        char = get_key_character(event, shift_pressed)
                        if len(key_name) == 1:
                            if shift_pressed and key_name in shift_number_map:
                                user_input.append(char)
                            else:
                                if count % 2 == 0:
                                    user_input.append(char.lower())
                                else:
                                    user_input.append(char.upper())
                        elif not char.isalnum() and len(char) == 1:
                            user_input.append(char)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift_pressed = False

    # Rendering
    screen.fill("black")

    if start:
        screen.blit(start_screen, start_screen_rect)
        screen.blit(space, space_rect)
    else:
        # Compare user input to the text and display it on screen
        colour = {}
        for i, letter in enumerate(text):
            if i < len(user_input):
                if user_input[i] == letter:
                    colour[i] = "green"
                else:
                    colour[i] = "red"
            else:
                colour[i] = "white"  # Not yet typed

        x_offset = 10
        y_offset = 10
        for i, letter in enumerate(text):
            if letter == '\n':  # Handle line breaks in the text
                letter_rendered = my_font.render('\\n', True, colour[i])
            elif letter == ' ':  # Handle space characters
                letter_rendered = my_font.render('_', True, colour[i])  # Display spaces as underscores
            else:
                letter_rendered = my_font.render(letter, True, colour[i])
            screen.blit(letter_rendered, (x_offset, y_offset))
            x_offset += letter_rendered.get_width()
            if x_offset > WINDOW_WIDTH - 20 or letter == '\n':
                x_offset = 10
                y_offset += LINE_HEIGHT

        type_speed = my_font.render(f"Type Speed: {speed}", True, "white")
        screen.blit(type_speed, type_speed_rect)

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
