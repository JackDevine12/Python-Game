#Import pygame, time and random modules
import pygame
import time
import random
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
green = (0,255,0)
bright_red = (200,0,0)
bright_green = (0,200,0)
#Define car width variable
car_width = 73
#Initialize clock object to help track time and frames per second
clock = pygame.time.Clock()

#Create a variable to track if the player has crashed or not
crashed = False
carImg = pygame.image.load('racecar.png')
#Define a function to draw a rectangle on the game display
def things(thingx, thingy, thingw, thingh, color):
    #Draw a rectangle on the game display using the specified x and y coordinates, width, height, and color
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#Define a function to display the number of things dodged on the game display
def things_dodged(count):
    #Create a font object using the specified font and size
    font = pygame.font.SysFont(None, 25)
    #Render the text to be displayed on the game display using the font object and color
    text = font.render("Dodged: "+str(count), True, black)
    #Draw the rendered text on the game display at the specified x and y coordinates
    gameDisplay.blit(text,(0,0))
#Define a function to draw the car image on the game display
def car(x,y):
    #Draw the car image on the game display at the x and y coordinates specified
    gameDisplay.blit(carImg, (x,y))
#Define a function to create a text surface object using the specified font and text
def text_objects(text, font):
    #Create a text surface object using the specified font and text
    textSurface = font.render(text, True, black)
    #Return the text surface object and its rectangular area
    return textSurface, textSurface.get_rect()
def message_display(text):
    #Create a font object using the specified font and size
    largeText = pygame.font.Font('freesansbold.ttf',115)
    #Call the text_objects function to create a text surface object and its rectangular area
    TextSurf, TextRect = text_objects(text, largeText)
    #Set the center of the rectangular area to the center of the game display
    TextRect.center = ((display_width/2),(display_height/2))
    #Draw the text surface object on the game display at the specified rectangular area
    gameDisplay.blit(TextSurf, TextRect)
    #Update the game display to show the changes made
    pygame.display.update()
    #Pause the game for 2 seconds to allow the player to read the message
    time.sleep(2)
    #Call the game_loop function to restart the game
    game_loop()

def crash():
    #Call the message_display function to show the "You Crashed" message on the game display
    message_display('You Crashed')
#Define a function to display the game introduction screen
def game_intro():
    #Create a variable to track if the game introduction screen is being displayed
    intro = True
    #While loop to keep the game introduction screen displayed until the user exits or starts the game
    while intro:
        #for loop to check for events that have occured since the last time the loop ran
        for event in pygame.event.get():
            #print the event to the console for debugging purposes
            print(event)
            #if the event is a quit event, exit the game
            if event.type == pygame.QUIT:
                #Update gameExit variable to True to exit the while loop
                pygame.quit()
                #quit the game and close the application
                quit()
        #Fill the game display with the color white
        gameDisplay.fill(white)
        #Create a font object using the specified font and size
        largeText = pygame.font.Font('freesansbold.ttf',115)
        #Call the text_objects function to create a text surface object and its rectangular area
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        #Set the center of the rectangular area to the center of the game display
        TextRect.center = ((display_width/2),(display_height/2))
        #Draw the text surface object on the game display at the specified rectangular area
        gameDisplay.blit(TextSurf, TextRect)
        #Mouse position variable to track the current position of the mouse cursor
        mouse = pygame.mouse.get_pos()
        #Check if the mouse cursor is within the bounds of the "Play" button
        if 150+100 > mouse[0] > 150 and 450 + 50 > mouse[1] > 450:
        #Create a button on the game display using a rectangle with the specified color, x and y coordinates, width, and height
            pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
        #Display the text "GO!" on the green button using a smaller font size
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("GO!", smallText)
        textRect.center = ( (150+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        #Check if the mouse cursor is within the bounds of the "Quit" button
        if 550+100 > mouse[0] > 550 and 450 + 50 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red,(550,450,100,50))
        else:
            pygame.draw.rect(gameDisplay, red,(550,450,100,50))
        #Display the text "QUIT" on the red button using a smaller font size
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = text_objects("QUIT!", smallText)
        textRect.center = ( (550+(100/2)), (450+(50/2)) )
        gameDisplay.blit(textSurf, textRect)
        #Update the game display to show the changes made
        pygame.display.update()
        #Set the clock to tick at 15 frames per second
        clock.tick(15)

def game_loop():
#Define the initial x and y coordinates for the car image
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    #Define the initial change in x and car speed variables
    x_change = 0
    car_speed = 0
    #Define the initial x and y coordinates, speed, width, and height for the rectangle
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100
    thingCount = 0
    dodged = 0
    #Define a variable to track if the game has exited or not
    gameExit = False
#While loop to keep the game running until the user crashes
    while not gameExit:
        #for loop to check for events that have occured since the last time the loop ran
        for event in pygame.event.get():
            #Check if the event is a quit event, if so set crashed to True to exit the while loop
            if event.type == pygame.QUIT:
                #Update gameExit variable to True to exit the while loop
                pygame.quit()
                quit()
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
        #Call the things function to draw a rectangle on the game display at the specified x and y coordinates, width, height, and color
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed
        #Call the car function to draw the car image on the game display at the specified x and y coordinates
        car(x,y)
        #Call the things_dodged function to display the number of things dodged on the game display
        things_dodged(dodged)
        #Check if the car has gone off the screen, if so set crashed to True to exit the while loop
        if x > display_width - car_width or x < 0:
            #If the car goes off the screen, call the crash function to display the crash message
            crash()
        #Check if the rectangle has gone off the screen, if so reset its y coordinate to the top of the screen and set its x coordinate to a random value within the display width
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)
        #Check if the car has collided with the rectangle, if so set crashed to True to exit the while loop
        if y < thing_starty+thing_height:
            print('y crossover')
            #Check if the car's x coordinate is within the rectangle's x coordinate range, if so call the crash function to display the crash message
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()
        #Fill the game display with a color, in this case white
        pygame.display.update()
        #Set the clock to tick at 60 frames per second
        clock.tick(60)
#Call the game_intro function to display the game introduction screen
game_intro()
#Call the game_loop function to start the game
game_loop()
#Quit pygame instance
pygame.quit()
#Quit python and application
quit()