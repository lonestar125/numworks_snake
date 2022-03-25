''' 
by lonestar125

original snake logic and some of the code from some random stackoverflow post 
because i couldnt be bothered to do the math
'''
import random
from kandinsky import *
from ion import *
from time import *

refresh = float(input("speed (0.1 - 1): ")) 
tilesize = int(input("tilesize (1-20): "))
boardWidth = 320
boardHeight = 210

class Snake():

    def __init__(self):

        self.snakeX = [tilesize, tilesize, tilesize]
        self.snakeY = []
        self.snakeLength = 3
        for i in range(self.snakeLength, 0, -1):
            self.snakeY.append(tilesize * i)
        print(self.snakeY)
        self.key = "s"
        self.points = 0

    def move(self):

        for i in range(self.snakeLength - 1, 0, -1):
                self.snakeX[i] = self.snakeX[i-1]
                self.snakeY[i] = self.snakeY[i-1]

        if self.key == "w":
            self.snakeY[0] = self.snakeY[0] - tilesize

        elif self.key == "s":
            self.snakeY[0] = self.snakeY[0] + tilesize

        elif self.key == "a":
            self.snakeX[0] = self.snakeX[0] - tilesize

        elif self.key == "d":
            self.snakeX[0] = self.snakeX[0] + tilesize

        self.eatApple()

    def eatApple(self):

        if self.snakeX[0] == apple.getAppleX() and self.snakeY[0] == apple.getAppleY():

            self.snakeLength = self.snakeLength + 1

            x = self.snakeX[len(self.snakeX) - 1] #grows
            y = self.snakeY[len(self.snakeY) - 1]
            self.snakeX.append(x + tilesize)
            self.snakeY.append(y)

            self.points = self.points + 1
            apple.createNewApple()

    def checkGameOver(self):

        for i in range(1, self.snakeLength, 1):

            if self.snakeY[0] == self.snakeY[i] and self.snakeX[0] == self.snakeX[i]:
                return False #eats itself

        if self.snakeX[0] < 0  or self.snakeX[0] > boardWidth or self.snakeY[0] < 0 or self.snakeY[0] > boardHeight:
            return False #out of bounds

        return True

    def getKey(self):

        if keydown(KEY_UP) == True:
            self.key = "w"
        elif keydown(KEY_DOWN) == True:
            self.key = "s"
        elif keydown(KEY_RIGHT) == True:
            self.key = "d"
        elif keydown(KEY_LEFT) == True:
            self.key = "a"

    def getSnakeX(self, index):
        return self.snakeX[index]

    def getSnakeY(self, index):
        return self.snakeY[index]

    def getSnakeLength(self):
        return self.snakeLength

    def getPoints(self):
        return self.points


class Apple:

    def __init__(self):
        self.appleX = tilesize * round(random.randint(tilesize, boardWidth - tilesize) / tilesize)
        self.appleY = tilesize * round(random.randint(tilesize, boardHeight - tilesize) / tilesize)

    def getAppleX(self):
        return self.appleX

    def getAppleY(self):
        return self.appleY

    def createNewApple(self):
        self.appleX = tilesize * round(random.randint(tilesize, boardWidth - tilesize) / tilesize)
        self.appleY = tilesize * round(random.randint(tilesize, boardHeight - tilesize) / tilesize)

snake = Snake()
apple = Apple()
game = snake.checkGameOver()

#gameloop
while game:

    #refresh/clear screen
    fill_rect(0, 0, 320, 210, "white")

    snake.move()
    if snake.checkGameOver() != False:
        #draw head
        fill_rect(snake.getSnakeX(0), snake.getSnakeY(0), tilesize, tilesize, "blue")
        
        #draw body
        for i in range(1, snake.getSnakeLength(), 1):
            fill_rect(snake.getSnakeX(i), snake.getSnakeY(i), tilesize, tilesize, "green") 
        
        #draw apple
        fill_rect(apple.getAppleX(), apple.getAppleY(), tilesize, tilesize, "red")

        #refresh rate
        sleep(refresh)

    #gameover msg
    else:
        fill_rect(0, 0, 320, 210, "white")
        draw_string("SCORE: " + str(snake.getPoints()), 110, 90, "black")
        sleep(2)
        break
    snake.getKey()
