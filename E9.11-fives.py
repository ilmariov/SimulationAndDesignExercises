from random import random

def main():
    printIntro()
    n = int(input('How many rolls to simulate? '))
    fives = simNRolls(n)
    print('Prob: {0:0.5%}'.format(fives/n))
 
def printIntro():
    print('''
    This program estimate the probability of getting a five of a kind in a single roll of five six-sided dice.
    ''')
 
def simNRolls(n):
    fives = 0
    for i in range(n):
        if simOneRollDice() == 5:
            fives = fives + 1
    return fives
 
def simOneRollDice():
    # it returns 5 if a five of a kind is rolled
    c = 0
    for i in range(5):
        if random() <= (1/6):
            c = c + 1
    return c
 
if __name__ == '__main__' : main()