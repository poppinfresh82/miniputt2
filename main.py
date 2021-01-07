from lib import assets
import pygame
from pygame.locals import *
import sys
import time
import mouse_events
import math

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

class Ball(pygame.sprite.Sprite):
    """
    Attributes: directionX, directionY, initialAngle, currentAngle, speed, image
    Methods:    update(), collide()
    """
    def __init__(self):
        super().__init__()
        self.image = assets.spritesGFX['ball']
        self.rect = self.image.get_rect()
        self.rect.center = (150,500)
        self.angle = math.radians(180+95)
        self.speed = 4
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.positionx = self.rect.center[0]
        self.positiony = self.rect.center[1]
        #self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed
        self.positionx += self.dx
        self.positiony += self.dy
        self.rect.center = (self.positionx, self.positiony)
        if self.speed > 0:
            self.speed = self.speed - 0.025
        else:
            self.speed = 0
        #print(self.dx, self.dy)
        #print(self.positionx,self.positiony)

    def bumperhit(self,bumper):
        alpha = math.degrees(self.angle) - bumper.angle
        bounceangle = 180 - 2*alpha + math.degrees(self.angle)
        self.angle = math.radians(bounceangle)
        self.dx = math.cos(self.angle) * self.speed
        self.dy = math.sin(self.angle) * self.speed


class Bumper(pygame.sprite.Sprite):
    """
    fadfda
    """
    def __init__(self,center_pixel):
        super().__init__()
        self.image = assets.spritesGFX['bumper45']
        self.angle = 45
        print(self.angle)
        #self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = center_pixel


        #self.shape = pygame.draw.line(screen, (122,122,122), self.start, self.end, width=4)



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
    gameBall = Ball()
    bumper1 = Bumper((150,300))
    ball_group = pygame.sprite.Group()
    ball_group.add(gameBall)                            # add game ball to sprite group ball_group (it's annoying but the only way to draw sprites in pygame is by groups)
    bumper_group = pygame.sprite.Group()
    bumper_group.add(bumper1)
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
        time.sleep(1/60)
        #renderMap(mapFile=currentMap, row=0, column=0)
        #splashScreen()
        screen.fill(color=(0,0,0))
        gameBall.update()
        ball_group.draw(screen)
        bumper_group.draw(screen)
        pygame.display.flip()
        bumper_hits = pygame.sprite.spritecollide(gameBall,bumper_group, False, pygame.sprite.collide_mask)
        if bumper_hits:
            gameBall.bumperhit(bumper1)



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