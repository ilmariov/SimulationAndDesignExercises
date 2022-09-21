from random import random
from graphics import *
import math

def main():
    n = int(input('How many steps? '))
    win = openGrid()
    nSteps(win, n)
    win.getMouse()
    win.close()

def openGrid():
    win = GraphWin('Opening grid', 100, 100)
    grid = Image(Point(50, 50), 'grid.gif')
    height = grid.getHeight()*13/20
    width = grid.getWidth()*13/20
    grid = GraphWin('Random Walk', width, height)
    grid.setCoords(-50, -50, 50, 50)
    placedPic = Image(Point(0, 0), 'grid.gif')
    placedPic.draw(grid)
    win.close()
    center = Circle(Point(0,0), 0.5)
    center.setFill('red')
    center.draw(grid)
    return grid

def nSteps(win, n):
    x = 0
    y = 0
    for i in range(n):
        angle = random() * 2 * math.pi
        newX = x + (math.cos(angle) * 3)
        newY = y + (math.sin(angle) * 3)
        Line(Point(x, y), Point(newX, newY)).draw(win)
        x = newX
        y = newY
    end = Circle(Point(x, y), 0.7)
    end.setFill('green')
    end.draw(win)


if __name__=='__main__' : main()