import math
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, scoredByA, scoredByB = simNGames(n, probA, probB)
    aScore, bScore, nGame, winner = bestGame(scoredByA, scoredByB)
    printSummary(winsA, winsB, nGame, winner, aScore, bScore)

def printIntro():
    print('This program simulates a game of racquetball between two')
    print('players called "A" and "B". The ability of each player is')
    print('indicated by a probability (a number between 0 and 1) that')
    print('the player wins the point when serving. Player A always')
    print('has the first serve.')

def getInputs():
    # Returns the three simulation parameters probA, probB and n
    a = float(input('What is the prob. player A wins a serve? '))
    b = float(input('What is the prob. player B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games and returns winsA and winsB
    winsA = 0
    winsB = 0
    scoredByA = []
    scoredByB = []
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i)
        scoredByA.append(scoreA)
        scoredByB.append(scoreB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB, scoredByA, scoredByB

def simOneGame(probA, probB, i):
    # i represents the number of the game match played
    scoreA = 0
    scoreB = 0
    if i%2 == 0:
        serving = "B"
    else:
        serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represents scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a==15 or b==15

def bestGame(scoredByA, scoredByB):
    theBest = 0
    nGame = 0
    winner = ''
    for i in range(len(scoredByA)):
        difference = abs(int(scoredByA[i]) - int(scoredByB[i]))
        if difference >= theBest:
            theBest = difference
            nGame = i
            if int(scoredByA[i]) > int(scoredByB[i]):
                winner = 'A'
            else:
                winner = 'B'
    return scoredByA[nGame], scoredByB[nGame], nGame, winner


def printSummary(winsA, winsB, nGame, winner, aScore, bScore):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print('\nGames simulated:', n)
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))
    print('\nThe best match played:')
    print('The {0}th match won by {1} with scores: {2} - {3}'.format(nGame, winner, aScore, bScore))

if __name__== '__main__' : main()