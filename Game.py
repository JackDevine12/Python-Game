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
#Define color variables using RGB values
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
#Define car width variable
car_width = 73
#Initialize clock object to help track time and frames per second
clock = pygame.time.Clock()

#Create a variable to track if the player has crashed or not
crashed = False
carImg = pygame.image.load('racecar.png')
#Define a function to draw the car image on the game display
def car(x,y):
    #Draw the car image on the game display at the x and y coordinates specified
    gameDisplay.blit(carImg, (x,y))
def game_loop():
#Define the initial x and y coordinates for the car image
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    #Define the initial change in x and car speed variables
    x_change = 0
    car_speed = 0
    #Define a variable to track if the game has exited or not
    gameExit = False
#While loop to keep the game running until the user crashes
    while not gameExit:
        #for loop to check for events that have occured since the last time the loop ran
        for event in pygame.event.get():
            #Check if the event is a quit event, if so set crashed to True to exit the while loop
            if event.type == pygame.QUIT:
                #Update gameExit variable to True to exit the while loop
                gameExit = True
            if event.type == pygame.KEYDOWN:
                #Check if the left arrow key is pressed, if so set x_change to -5 to move the car left
                if event.key == pygame.K_LEFT:
                    x_change = -5
                #Check if the right arrow key is pressed, if so set x_change to 5 to move the car right
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                #Check if the left or right arrow key is released, if so set x_change to 0 to stop the car
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        #Fill the game display with the color white
        gameDisplay.fill(white)
        #Call the car function to draw the car image on the game display at the specified x and y coordinates
        car(x,y)
        #Check if the car has gone off the screen, if so set crashed to True to exit the while loop
        if x > display_width - car_width or x < 0:
            #If the car goes off the screen, set crashed to True to exit the while loop
            gameExit = True
        #Print event variable value
        print(event)
        #Fill the game display with a color, in this case white
        pygame.display.update()
        #Set the clock to tick at 60 frames per second
        clock.tick(60)
#Call the game_loop function to start the game
game_loop()
#Quit pygame instance
pygame.quit()
#Quit python and application
quit()