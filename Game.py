#Import pygame module
import pygame
#Intailise pygame object
pygame.init()
#Define game display object, 800px wide and 600px tall
gameDisplay = pygame.display.set_mode((800,600))
#Define game caption/title of game window
pygame.display.set_caption('A bit Racey')
#Initialize clock object to help track time
clock = pygame.time.Clock()