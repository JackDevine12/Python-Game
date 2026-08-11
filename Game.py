#Import pygame module
import pygame
#Intailise pygame object
pygame.init()
#Define display width and height variables
display_width = 800
display_height = 600
#Define game display object using the display width and height variables
gameDisplay = pygame.display.set_mode((display_width,display_height))
#Define game caption/title of game window
pygame.display.set_caption('A bit Racey')
#Initialize clock object to help track time and frames per second
clock = pygame.time.Clock()

#Create a variable to track if the player has crashed or not
crashed = False
#While loop to keep the game running until the user crashes
while not crashed:
    #for loop to check for events that have occured since the last time the loop ran
    for event in pygame.event.get():
        #Check if the event is a quit event, if so set crashed to True to exit the while loop
        if event.type == pygame.QUIT:
            #Update crashed variable to True to exit the while loop
            crashed = True
        #Print event variable value
        print(event)
    #Fill the game display with a color, in this case white
    pygame.display.update()
    #Set the clock to tick at 60 frames per second
    clock.tick(60)
#Quit pygame instance
pygame.quit()
#Quit python and application
quit()