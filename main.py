import pygame
import numpy as np
import scipy
from board import Board
from graphic import Graphic
from NeuralNetwork import NN




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
        self.Network = NN(784, 10, 200, 0.1)

    def TransponesCoords(self, pos, mouse):
        x, y = pos
        if(x >= self.BoardX) and (x <= self.BoardX + self.BOARD.get_width()) and (y >= self.BoardY) and (y <= self.BOARD.get_height() + self.BoardY):
            x -= self.BoardX
            y -= self.BoardY
            self.BOARD.DrawCell((x, y),  (mouse, mouse, mouse))

    def Draw(self):
        self.WINDOW.fill((255, 255, 255))
        self.BOARD.draw() 
        self.GRAPHIC.draw()
        self.WINDOW.blit(self.GRAPHIC.WIN, (self.GraphicX, self.GraphicY))
        self.WINDOW.blit(self.BOARD.WIN, (self.BoardX, self.BoardY))
        pygame.display.update()

    def PrepareBoard(self):
        data = []
        for row in self.BOARD.arr:
            for color in row:
                data.append(color[0])
        
        res = (np.asfarray(data) / 255.0 * 0.99) + 0.01
        return res

    def TrainNN(self, eras):
        trainig_data = open("mnist_train.csv", 'r')
        trainig_list = trainig_data.readlines()
        trainig_data.close()
        for e in range(eras):
            for data in trainig_list:
                all_vals = data.split(',')
                # for i in range(1, len(all_vals)):
                #     if all_vals[i] != 0:
                #         all_vals[i] = 234
                inputs = (np.asfarray(all_vals[1:]) / 255.0 * 0.99) + 0.01
                tragets = np.zeros(10) + 0.01
                tragets[int(all_vals[0])] = 0.99
                self.Network.Training(inputs, tragets)

    def Loop(self):
        loops = True
        while loops:
            self.timer.tick(144)
            self.Draw()

            inputs = self.PrepareBoard()

            res = self.Network.Query(inputs)

            vals = []
            for val in res:
                vals.append(val)

            self.GRAPHIC.update_vals(vals)

            ans = np.argmax(res)

            self.GRAPHIC.ChangeMaxVal(ans)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    loops = False
                    break
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    self.TransponesCoords(pos, 234)
                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    self.TransponesCoords(pos, 0)

        pygame.quit()



game = App(1005, 800, 300, 0, 0, 0)

game.TrainNN(1)

scored = []


# test_data = open("mnist_test.csv", 'r')
# test_list = test_data.readlines()
# test_data.close()

# for test in test_list:
#     test_vals = test.split(',')
#     correct = int(test_vals[0])
#     inputs = (np.asfarray(test_vals[1:]) / 255.0 * 0.99) + 0.01
#     res = game.Network.Query(inputs)
#     ans = np.argmax(res)

#     print("The network answer is", ans)

#     if(ans == correct):
#         scored.append(1)
#     else:
#         scored.append(0)


# scored = np.asarray(scored)

# print("The persent of truth answers is", scored.sum() / scored.size * 100 ,'%')


game.Loop()