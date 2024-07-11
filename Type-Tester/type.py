import time

#Imports and Technicalities
import pygame
from games_funcs import generate_paragraph,wrapline,get_key_character,shift_number_map


pygame.font.init()




text = generate_paragraph()

#Fonts
my_font = pygame.font.SysFont('Comic Sans MS', 20)

#Text
new_text = wrapline(text,my_font,1000)
Paragraph = my_font.render(f"{text}",True,"white",wraplength=900)

#Score 
speed = 0
#Text rectangles and rendering
start_screen = my_font.render("START TYPE RACER",True,"white",wraplength=900)
space = my_font.render("Press ANY KEY to Play",True,"white",wraplength=900)
type_speed = my_font.render(f"Type Speed: {speed} ",True,"white",wraplength=900)
type_speed_rect = type_speed.get_rect(center=(500,800))
start_screen_rect = start_screen.get_rect(center=(500,100))
space_rect = space.get_rect(center=(500,800))
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Type Racer')
shift_pressed = False
start = True



text_leveler = 0

while running:
    if start:
         screen.fill("black")
         screen.blit(start_screen,start_screen_rect)
         screen.blit(space,space_rect)
    elif not start:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # write text 
        screen.blit(Paragraph,(0,0))
        screen.blit(type_speed,type_speed_rect) 

        #keys 
        keys = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and start == True:
             start = False
             user_input = []
             count = 0
        elif start == False:
            if event.type == pygame.KEYDOWN:
        #each item in a list has a numerical value
                length = len(text)
                #have a list with what the user has typed 
                if event.key:
                        
                        if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                            shift_pressed = True
                        else:
                            if pygame.key.name(event.key).lower() == "caps lock":
                                count +=1
                            if pygame.key.name(event.key).lower() == "backspace":
                                try: 
                                    user_input.pop()
                                except IndexError:
                                    pass
                            if pygame.key.name(event.key).lower() == "space":
                                user_input.append(" ")
                        
                            else:
                                _ = get_key_character(event,shift_pressed)
                                if _.isalpha() == False and _.isdigit() == False and len(_) < 2:
                                    user_input.append(_)
                                
                            statement = len(pygame.key.name(event.key)) > 2 
                            if statement == False: 
                                if (count % 2) == 0:
                                    user_input.append(pygame.key.name(event.key))
                                else: user_input.append(pygame.key.name(event.key).upper())
                            else:
                                print("True",statement)
                        print(user_input)
                #compare it to the text
                #if user pressed backspace remove items from list
                #special characters should be added to the list differently.
            #we can add plus 1 to get the next numerical value
            #if we hit the end of the list we will know because plus 1 will give us an index Error
                       
                print(pygame.key.name(event.key))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift_pressed = False

      
            

  


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()