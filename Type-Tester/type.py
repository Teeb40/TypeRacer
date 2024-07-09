import time

#Imports and Technicalities
import pygame
from games_funcs import generate_paragraph,wrapline


pygame.font.init()




text = generate_paragraph()

#Fonts
my_font = pygame.font.SysFont('Comic Sans MS', 20)


new_text = wrapline(text,my_font,1000)
Paragraph = my_font.render(f"{text}",True,"white",wraplength=900)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Type Racer')



text_leveler = 0

while running:

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # write text 
    screen.blit(Paragraph,(0,0))
    

    #keys 
    keys = pygame.key.get_pressed()
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("Avacado")
            for texts in new_text:
                for letters in texts:
                        ...
                        
            

  


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()