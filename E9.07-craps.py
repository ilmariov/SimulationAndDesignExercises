from random import randint

def main():
    printIntro()
    n = int(input('\nHow many games to simulate? '))
    wins = simNGames(n)
    printProb(n, wins)

def printIntro():
    print('''
    This program simulates n games of craps to estimate the probability
    that the player wins
    ''')

def simNGames(n):
    wins = 0
    for i in range(n):
        if simOneGame():
            wins = wins + 1
    return wins

def simOneGame():
    # This function checks if the player wins or loses the game
    # it prints True if wins, False otherwise.
    initial = randint(2,12)
    checker = None
    if initial==2 or initial==3 or initial==12:
        checker = False
    elif initial==7 or initial==11:
        checker = True
    else:
        new_roll = 0
        while new_roll != initial and new_roll != 7:
            new_roll = randint(2,12)
            if new_roll == 7:
                checker = False
            elif new_roll == initial:
                checker = True
    return checker

def printProb(n, wins):
    print('\nAfter simultaing {} games of craps, the estimated'.format(n))
    print('probability of winning is: {0:0.1%}'.format(wins/n))


if __name__ == '__main__' : main()