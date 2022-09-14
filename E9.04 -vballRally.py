from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print('This program simulates a game of volleyball between two')
    print('players called "A" and "B" that play using rally scoring.')
    print('The ability of each player is indicated by a probability')
    print('(a number between 0 and 1) that the player wins the point')
    print('when serving. Player A always has the first serve and players')
    print("can score even if they are not serving.")

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
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represents scores for a volleyball game
    # Returns True if the game is over, False otherwise.
    return (a>=25 or b>=25) and abs(a-b)>=2

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print('\nGames simulated:', n)
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

if __name__== '__main__' : main()