import os
import sys
import pygame 
from pygame.locals import *
from . import board 

os.environ['SDL_VIDEO_CENTERED'] = '1'

class GuiChessGame:
    colours = {
        'Ash': (50, 50, 50),
        'White': (255, 255, 255),
        'Black': (0, 0, 0)
    }

    def __init__(self, title='Chess!'):
        self.FPS = 30
        self.FPSCLOCK = pygame.time.Clock()
        self.SURFACE = None 
        self.FONT = None 
        self.gameboard = None
        self.WWIDTH = 600
        self.WHEIGHT = 600
        self.FONTSIZE = 30
        self.BGCOLOUR = self.colours['Ash']
        self.TITLE = title

    def start(self, fen=''):
        pygame.init()

        # Draw the window 
        self.SURFACE = pygame.display.set_mode((self.WWIDTH, self.WHEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.FONT = pygame.font.SysFont('calibri', self.FONTSIZE)

        # Check for a quit (?)
        self.check_for_quit()

        self.SURFACE.fill(self.BGCOLOUR)
        self.gameboard = board.Board(self.colours, self.BGCOLOUR, self.SURFACE)
        self.gameboard.displayBoard()

        if (fen):
            self.gameboard.updatePieces(fen)
        else:
            self.gameboard.drawPieces()

        pygame.display.update()
        self.FPSCLOCK.tick(self.FPS)
    
    def check_for_quit(self):
        for event in pygame.event.get(QUIT):
            self._terminate()
        for event in pygame.event.get(KEYUP):
            if event.key == K_ESCAPE:
                self._terminate()
            pygame.event.post(event)
        
        return False

    
    def update(self, fen):
        self.check_for_quit()
        self.gameboard.displayBoard()
        self.gameboard.updatePieces(fen)

        pygame.display.update()
        self.FPSCLOCK.tick(self.FPS)

    def _terminate(self):
        pygame.quit()
        sys.exit()

    
    def highlight_square(self, square):
        print(self.gameboard.boardRect)
        
    
