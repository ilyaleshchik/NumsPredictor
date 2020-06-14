import pygame

pygame.font.init()

class Graphic:
    def __init__(self, W, H, FONT, FONTSIZE, linesize):
        self.WIDTH = W
        self.HEIGHT = H
        self.FONT = pygame.font.SysFont(FONT, FONTSIZE)
        self.vals = [0.0] * 10
        self.timer = pygame.time.Clock()
        self.WIN = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.MAXVAL = 0
        self.LINESIZE = linesize

    def draw(self):
        self.WIN.fill((255, 255, 255))
        labels = []
        for i in range(10):
            labels.append(self.FONT.render(f'{i}', 1, (0, 0, 0)))
        lstY = 20
        for i in range(10):
            self.WIN.blit(labels[i], (50, lstY + 10))
            pygame.draw.rect(self.WIN, (40, 191, 141), (80, lstY + 10 + labels[i].get_height() // 2 - 5, self.LINESIZE, 10))
            pygame.draw.rect(self.WIN, (237, 0, 0), (80, lstY + 10 + labels[i].get_height() // 2 - 5, self.LINESIZE * self.vals[i], 10))
            lstY += 10
            lstY += labels[i].get_height()
        
        cur_font = pygame.font.SysFont("IMPACT", 20)

        max_label = cur_font.render(f'{self.MAXVAL} is answer now!', 1, (0, 0, 0))
        self.WIN.blit(max_label, (100, 450))

    def ChangeMaxVal(self, cur):
        self.MAXVAL = cur

    def update_max(self, newVal):
        self.MAXVAL = newVal


    def update_vals(self, arr):
        self.vals = arr