from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsAReg, winsBReg, winsARally, winsBRally = simNGames(n, probA, probB)
    printSummary(winsAReg, winsBReg, winsARally, winsBRally)

def printIntro():
    print('''
    This program compares regular volleyball games to those using rally scoring. 
    This returns results whether rally scoring magnifies, reduces, or has no 
    effect on the relative advantage enjoyed by the better team.''')
    
def getInputs():
    a = float(input('\nWhat is the prob. team A wins a serve? '))
    b = float(input('What is the prob. team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games and returns matches won by each team for regular and rally scoring.
    winsAReg = 0
    winsBReg = 0
    winsARally = 0
    winsBRally = 0
    for i in range(n):
        scoreAReg, scoreBReg = simOneGameReg(probA, probB)
        if scoreAReg > scoreBReg:
            winsAReg = winsAReg + 1
        else:
            winsBReg = winsBReg + 1
        scoreARally, scoreBRally = simOneGameRally(probA, probB)
        if scoreARally > scoreBRally:
            winsARally = winsARally + 1
        else:
            winsBRally = winsBRally + 1
    return winsAReg, winsBReg, winsARally, winsBRally

def simOneGameReg(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOverReg(scoreA, scoreB):
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

def gameOverReg(a, b):
    # a and b represents scores for a regular volleyball game
    # Returns True if the game is over, False otherwise.
    return (a>=15 or b>=15) and abs(a-b)>=2

def simOneGameRally(probA, probB):
    scoreA = 0
    scoreB = 0
    serving = "A"
    while not gameOverRally(scoreA, scoreB):
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

def gameOverRally(a, b):
    # a and b represents scores for a rally scoring volleyball game
    # Returns True if the game is over, False otherwise.
    return (a>=25 or b>=25) and abs(a-b)>=2

def result(reg, ral):
    # Returns the string to be added in comparison summary.
    string = ''
    if (ral - reg) > 0:
        string = 'magnified'
    elif ral==reg:
        string = 'had no effect on'
    else:
        string = 'reduced'
    return string

def compareGames(a, b, A, B):
    winner = ''
    string = ''
    if a > b:
        string = result(a, A)
        winner = 'A'
    else:
        string = result(b, B)
        winner = 'B'
    return string, winner

def printSummary(winsAReg, winsBReg, winsARally, winsBRally):
    # Prints a summary of wins for each team and each type of game
    # Reports the outcome of the investigation when comparing.
    n = winsAReg + winsBReg
    outcome, winner = compareGames(winsAReg, winsBReg, winsARally, winsBRally)
    print('\nGames simulated:', n)
    print('\nScoring playing regular volleyball:')
    print('Wins for team A: {0} ({1:0.1%})'.format(winsAReg, winsAReg/n))
    print('Wins for team B: {0} ({1:0.1%})'.format(winsBReg, winsBReg/n))
    print('\nResults using rally scoring:')
    print('Wins for team A: {0} ({1:0.1%})'.format(winsARally, winsARally/n))
    print('Wins for team B: {0} ({1:0.1%})'.format(winsBRally, winsBRally/n))
    print('\nRally scoring', outcome + ' the relative advantage enjoyed by team', winner)


if __name__== '__main__' : main()