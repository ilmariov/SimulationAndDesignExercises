# A program to calculate a random float in the range -0.5 - 0.5

from random import random, randrange, randint, uniform

def main():
    num = randrange(-1,3,2)*random()
    while not(-0.5 <= num <=0.5):
        num = randrange(-1,3,2)*random()
    print(num)

def sixSidedDie():
    print(randint(1,6))

def sumDices():
    sum = randint(1,6) + randint(1,6)
    print(sum)

def randFloat():
    print(uniform(-0.5,0.5))

if __name__== '__main__': randFloat()