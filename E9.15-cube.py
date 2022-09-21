from random import random

def main():
    printIntro()
    n = int(input('How many looks? '))
    times = seeWall(n)
    print('\nTimes that the wall is seen:', times)

def printIntro():
    print('''
    Assuming that you are located in the exact center of a cube, and that if you could look
    all around you in every direction, each wall of the cube would occupy 1/6 of your field
    of vision. Now, if you move toward one of the walls so that you are now halfway between 
    it and the center of the cube, the fraction of your field of vision that is now taken up
    by the closest wall is: 2/3
    ''')

def seeWall(n):
    c = 0
    for i in range(n):
        if random() <= 1/6:
            c = c + 1
    return c


if __name__=='__main__' : main()