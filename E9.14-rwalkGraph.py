from random import random
from graphics import *

def main():
    #n = int(input('How many steps? '))
    grid = openGrid()
    grid.getMouse()
    grid.close()

def openGrid():
    win = GraphWin('Opening grid', 100, 100)
    grid = Image(Point(50, 50), 'grid.gif')
    height = grid.getHeight()*13/20
    width = grid.getWidth()*13/20
    window = GraphWin('Random Walk', width, height)
    window.setCoords((-width/2), (-height/2), (width/2), (height/2))
    placedPic = Image(Point(0, 0), 'grid.gif')
    placedPic.draw(window)
    win.close()
    center = Circle(Point(0,0), 2.5)
    center.setFill('red')
    center.draw(window)
    return window

if __name__=='__main__' : main()