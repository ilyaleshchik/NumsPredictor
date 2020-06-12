import pygame
import numpy
import scipy
from board import Board
from graphic import Graphic


class App:
    def __init__(self, W, H, BOARDX, BOARDY, GraphicX, GraphicY):
        self.WIDTH = W
        self.HEIGHT = H
        self.BoardX = BOARDX
        self.BoardY = BOARDY
        self.GraphicX = GraphicX
        self.GraphicY = GraphicY
        self.WINDOW = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.timer = pygame.time.Clock()
        self.BOARD = Board(28, 28, 25)
        self.GRAPHIC = Graphic(300, 500, "IMPACT", 25, 200)


    def Draw(self):
        self.WINDOW.fill((0, 0, 0))
        self.BOARD.draw()
        self.GRAPHIC.draw()
        self.WINDOW.blit(self.GRAPHIC.WIN, (self.GraphicX, self.GraphicY))
        self.WINDOW.blit(self.BOARD.WIN, (self.BoardX, self.BoardY))
        pygame.display.update()

    def Loop(self):
        loops = True
        while loops:
            self.timer.tick(144)
            self.Draw()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    loops = False
                    break
        pygame.quit()



game = App(1000, 1000, 300, 0, 0, 0)
game.Loop()