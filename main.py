from lib import assets
import pygame
from pygame.locals import *
import sys
import time
import mouse_events

pygame.init()  # starts the pygame environment
#instantiate screen object
screenx = 640
screeny = 640
screen = pygame.display.set_mode((screenx,screeny))
pygame.display.set_caption('MINIPUTT')
game_font = pygame.font.SysFont('arialblack', 20)
icon = pygame.image.load('./textures/grass_2.png')
pygame.display.set_icon(icon)
currentMap = assets.mapsGFX['MAP_1']

class Game:
    """
    Game class handles all the permanent game stats such as score, maps
    Also keeps track of game state such as mode (splash screen, main game, paused, etc)
    """
    def __init__(self):
        self.gameMode = 'splash'


def renderMap(mapFile, row, column):
    screen.blit(mapFile, (row, column))    # blit takes two arguments: source, destination
                                           # in this case location = currentMap desination = (0,0) top left
def splashScreen():

    #drawing text:
    #font.render() is the method to make a text object that is then blit()
    #blit() pushes a surface on the "shadow" video buffer, that is flipped
    #render() takes up to four arguments:
    #render(text,antialias,colour, background=None) --> surface
    #text = a string literal or object
    #antialias = takes an 8 bit image and "smooths it" by remapping it as a 24 bit image
    #colour = (r,g,b) tuple
    #background = if None than transparent
    word = game_font.render('Hello World', None, (123, 111, 202))
    screen.blit(word, (screenx/2, screeny/2))
    pygame.display.flip()








def main():
    game = Game()
    mouseEvents = mouse_events.MouseEvents(screen)
    splashScreen()
    while True:
        """
        POLL FOR KEY/MOUSE EVENTS
        """
        for event in pygame.event.get():               # iterate the event stack
            if event.type == pygame.QUIT:
                pygame.quit()                          # closes pygame
                sys.exit()                             # releases system resources
            if event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                print("x:", mx, " y:", my)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print("x:", mx, " y:", my)
                mouseEvents.mouseDown(game, pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                pass
        """
        RENDERING MAP, SPRITES    
        """
        time.sleep(1/60)                                #limit event polling to 60 times per second
        renderMap(mapFile=currentMap, row=0, column=0)  #currentMap will change as we advance in the game
        pygame.display.flip()                           # so it doesn't make sense to hardcode it
                                                        # the var currentMap will be updated


main()
"""
Assets:
What game objects will need graphical representation?
Which of those will interact with each other (graphically)

over the holidays assets:
splash screen background
reorient buttons 
delete hello world
backgrounds for rooms (living room) (rail yard)
sprites for interactive objects (chair intact, chair broken, fireplace dormant, fireplace lit, assassins)
16x16 pngs for inventory items (maybe?)
backgrounds can be .jpg , sprites have to be .png
link assets to assets.py
    three dictionaries:
        maps = {}
        sprites = {}
        items = {}



"""