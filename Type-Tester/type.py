import time
import pygame
from games_funcs import generate_paragraph, wrapline, get_key_character, shift_number_map

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FONT_SIZE = 30
LINE_HEIGHT = FONT_SIZE + 5



# Initialize fonts
my_font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)

# # Wrap the text
# wrapped_text = wrapline(text, my_font, WINDOW_WIDTH - 20)

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
game_over = False
while running:
    mouse = pygame.mouse.get_pos()
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and start:
            # Generate text for the game
            text = generate_paragraph()
            start = False
            user_input = []
            count = 0
            char_count = 0
            acc_char_count = 0
            checker = 0
            colour = {}
        elif not start:
            if event.type == pygame.KEYDOWN:
                char_count += 1 
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
                            if char_count <= 0: pass
                            else: char_count -=1
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
      

    elif not start and not game_over:
        
        #timer
        time_ = int(round((pygame.time.get_ticks()/1000)/60,0))
        # Compare user input to the text and display it on screen
        colour = {}
        for i, letter in enumerate(text):
            if i < len(user_input):
                if user_input[i] == letter:
                    colour[i] = "green"
                    acc_char_count +=1 
                else:
                    colour[i] = "red"
                    acc_char_count -=1
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
        try:
            speed = ((char_count/5)/time_)
        except ZeroDivisionError:
            pass
        
        type_speed = my_font.render(f"Type Speed: {int(round(speed,0))} ('_' are Spaces)", True, "white")
        screen.blit(type_speed, type_speed_rect)
        
        #check if game is finished
        if len(user_input) == len(text):
            if "red" not in colour.values():
                game_over = True
            else:
                pass

    elif game_over:
        
        end = my_font.render("Text Complete", True, "white")
        repeat = my_font.render("Try Again?", True, "white")
        type_speed = my_font.render(f"Type Speed: {int(round(speed,0))}", True, "white")
        repeat_rect = repeat.get_rect(center=(500,500))
        end_rect = end.get_rect(center=(500,100))
        screen.blit(end,end_rect)
        screen.blit(repeat,repeat_rect)
        screen.blit(type_speed, type_speed_rect)
        
        try:
            speed = ((char_count/5)/time_)
        except ZeroDivisionError:
            pass
        if repeat_rect.collidepoint(mouse) and event.type == pygame.MOUSEBUTTONDOWN:
            game_over = False
            start = True

        

    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

pygame.quit()
