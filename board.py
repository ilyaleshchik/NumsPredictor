import pygame
import random

def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


class Board:
    def __init__(self, W, H):
        self.WIDTH = W * 25 + 1
        self.HEIGHT = H * 25 + 1
        self.timer = pygame.time.Clock()
        self.WIN =  pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.arr = []
        for i in range(H):
            self.arr.append([])
            for j in range(W):
               self.arr[-1].append((255, 255, 255))


    def draw(self):
        self.WIN.fill((0, 0, 0))

        for i in range(self.HEIGHT // 25):
            for j in range(self.WIDTH // 25):
                pygame.draw.rect(self.WIN, self.arr[i][j] , (j * 25 + 1, i * 25 + 1, 24, 24))
        pygame.display.update()


    def DrawCell(self, pos, color):
        x , y = pos[0], pos[1]
        x //= 25
        y //= 25
        if(x >= self.HEIGHT // 25):
            x = self.HEIGHT // 25 - 1
        if y >= self.HEIGHT // 25:
            y = self.HEIGHT // 25 - 1
        self.arr[y][x] = color
    

    def Run(self):
        run = True
        while run:
            self.timer.tick(144)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            mouse_statements = pygame.mouse.get_pressed()
            if mouse_statements[0] == 1:
                pos = pygame.mouse.get_pos()
                self.DrawCell(pos, (0, 0, 0))
            if mouse_statements[2] == 1:
                pos = pygame.mouse.get_pos()
                self.DrawCell(pos, (255, 255, 255))



b = Board(50, 50)

b.Run()