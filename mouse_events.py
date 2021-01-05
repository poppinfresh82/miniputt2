class MouseEvents:
    def __init__(self, screen):
        self.screen = screen

    def mouseDown(self, game, mousePosition):
        if game.gameMode == 'splash':
            if mousePosition[0] in range(100,200) and mousePosition[1] in range(150,250):
                print('you clicked in the 50x50 box')

    #def mouseMove(self):


""" your mission for next time (Friday) 
make your program print a message when you click "start game" on the splash screen
make your program quit when you click quit
put a "load game" in your splash screen, this won't work yet

"""
