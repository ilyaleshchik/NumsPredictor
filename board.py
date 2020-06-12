import pygame
import random

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


class Board():
    def __init__(self, W, H, TOPIXEL):
        self.WIDTH = W * TOPIXEL + 1
        self.HEIGHT = H * TOPIXEL + 1
        self.PIXELWIDTH = TOPIXEL
        self.W = W
        self.H = H
        self.timer = pygame.time.Clock()
        self.WIN = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.arr = []
        for i in range(self.H):
            self.arr.append([])
            for j in range(self.W):
               self.arr[-1].append((255, 255, 255))


    def draw(self):
        # self.WIN.fill((0, 0, 0))

        for i in range(self.H):
            for j in range(self.W):
                pygame.draw.rect(self.WIN, self.arr[i][j] , (j * self.PIXELWIDTH + 1, i * self.PIXELWIDTH + 1, self.PIXELWIDTH - 1, self.PIXELWIDTH - 1))


    def DrawCell(self, pos, color):
        x , y = pos[0], pos[1]
        x //= self.PIXELWIDTH
        y //= self.PIXELWIDTH
        if(x >= self.HEIGHT // self.PIXELWIDTH):
            x = self.HEIGHT // self.PIXELWIDTH - 1
        if y >= self.HEIGHT // self.PIXELWIDTH:
            y = self.HEIGHT // self.PIXELWIDTH - 1
        self.arr[y][x] = color
    

    # def Run(self):
    #     run = True
    #     while run:
    #         self.timer.tick(144)
    #         self.draw()

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #                 break
    #         mouse_statements = pygame.mouse.get_pressed()
    #         if mouse_statements[0] == 1:
    #             pos = pygame.mouse.get_pos()
    #             self.DrawCell(pos, (0, 0, 0))
    #         if mouse_statements[2] == 1:
    #             pos = pygame.mouse.get_pos()
    #             self.DrawCell(pos, (255, 255, 255))

