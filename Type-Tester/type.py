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
colour = {}


text_leveler = 0

while running:
   
    

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
                length = len(text)
                #have a list with what the user has typed 
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift_pressed = True
                else:
                    key_name = pygame.key.name(event.key).lower()
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
                                    user_input.append(char)
                                else:
                                    user_input.append(char.upper())
                        elif not char.isalnum() and len(char) == 1:
                            user_input.append(char)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                    shift_pressed = False
            print(user_input)
                #compare it to the text and display it on screen
            #loop through the user_input 
            if user_input:
                x = 0 
                colour = {}
                for input in user_input:
                   #compare it to the text on the screen letter by letter
                   x +=1
                   if text[x] == input:
                       colour.update({text[x]:"Green"})
                   else:
                       colour.update({text[x]:"Green"})
            #if a letter is in input and wrong then display a red letter for that letter in the text
            #if it is correct show a green letter 
            #if the input does not exist keep the letter as white
    if start:
         screen.fill("black")
         screen.blit(start_screen,start_screen_rect)
         screen.blit(space,space_rect)
    elif not start:
        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        # write text 
        for letter in text:
            if letter in colour:
                letter_ = my_font.render(f"{letter}",True,colour[letter],wraplength=900)
            else:
              q= 0
              q +=1 
              letter_ = my_font.render(f"{letter}",True,"white",wraplength=900)
              screen.blit(letter_,(0,q))
                
        screen.blit(type_speed,type_speed_rect) 



         
                       
            
      
            

  


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()