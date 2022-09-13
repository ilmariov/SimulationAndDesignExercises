# A program to calculate a random float in the range -0.5 - 0.5

from random import random, randrange

def main():
    num = randrange(-1,3,2)*random()
    while not(-0.5 <= num <=0.5):
        num = randrange(-1,3,2)*random()
    print(num)

if __name__== '__main__': main()