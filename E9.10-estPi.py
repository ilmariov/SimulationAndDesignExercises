from random import random

def main():
    printIntro()
    n = int(input('\nHow many darts to throw? '))
    aproxPi = estimatePi(n)
    print('\nAfter throwing {0} darts we estimate the value of pi as: {1}'.format(n, aproxPi))

def printIntro():
    print('''
    This program estimates the number of pi from throwing darts 
    to a round dartboard within a square cabinet.
    ''')

def estimatePi(n):
    h = 0
    for i in range(n):
        x = (2 * random()) - 1
        y = (2 * random()) - 1
        if (x**2 + y**2 <= 1):
            h = h + 1
    aproxPi = 4 * (h / n)
    return aproxPi


if __name__=='__main__' : main()