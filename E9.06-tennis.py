from ast import Num
from curses import set_tabsize
from random import randint, random

from Sample_codes.rball import gameOver, simOneGame

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNMatches(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print('''
    This program simulates a match of tennis between two players or teams
    called 'A' and 'B'. The ability of each player or team is indicated by
    a probability (a number between 0 and 1) that the player or team wins
    the point when serving. First server is chosen ramdomly.
    ''')
    
def getInputs():
    a = float(input('\nWhat is the prob. player or team A wins a serve? '))
    b = float(input('What is the prob. player or team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n

def simNMatches(n):
    winsA = 0
    winsB = 0
    for i in range(n):
        setsA, setsB = simOneMatch()
        if setsA > setsB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def firstGame(setsA, setsB):
    return setsA==0 and setsB==0

def matchOver(a, b):
    # a and b represents won sets for a tennis match
    # Returns True if the match is over, False otherwise.
    return (a>=2 or b>=2) and abs(a-b)>=1

def whoServes():
    num = randint(0,1)
    if num == 0:
        serving = 'A'
    else:
        serving = 'B'
    return serving

def gameOver(a, b):
    # a and b represents scores for a tennis game
    # Returns True if the game is over, False otherwise.
    return (a>=4 or b>=4) and abs(a-b)>=2

def simOneMatch(probA, probB):
    setsA = 0
    setsB = 0
    gamesA = 0
    gamesB = 0
    scoreA = 0
    scoreB = 0
    while not matchOver(setsA, setsB):
        while not setOver(gamesA, gamesB):
            if setsA==0 and setsB==0:
                serve = whoServes
                while not gameOver(scoreA, scoreB):
                    scoreA, scoreB, serving = simOneGame(serve, probA, probB)
                gamesA, gamesB, serve = simOneSet(serving, scoreA, scoreB)
                if gamesA > gamesB:
                    setsA = setsA + 1
                else:
                    setsB = setsB + 1
            else:
                while not gameOver(scoreA, scoreB):
                    scoreA, scoreB, serving = simOneGame(serving, probA, probB)
                gamesA, gamesB, serving = simOneSet(serving, scoreA, scoreB)
                if gamesA > gamesB:
                    setsA = setsA + 1
                else:
                    setsB = setsB + 1
    return setsA, setsB

def setOver(a, b):
    # a and b represents won games for a tennis set
    # Returns True if the set is over, False otherwise.
    check = False
    if (a==6 or b==6) and abs(a-b)>=2:
        check = True
    elif (a==5 and b==7) or (a==7 and b==5):
        check = True
    elif (a==6 and b==7) or (a==7 and b==6):
        check = True
    return check

def simOneSet(serving, scoreA, scoreB):
    wonGamesA = 0
    wonGamesB = 0
    while not setOver(wonGamesA, wonGamesB):
        if scoreA > scoreB:
            wonGamesA = wonGamesA + 1
        else:
            wonGamesB = wonGamesB + 1
    return wonGamesA, wonGamesB, serving

def simOneGame(serving, probA, probB):
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = 'B'
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = 'A'        
    return scoreA, scoreB, serving
        
def simNMatches(n, probA, probB):
    # Simulates n games and returns winsA and winsB
    winsA = 0
    winsB = 0
    for i in range(n):
        setsA, setsB = simOneMatch(probA, probB)
        if setsA > setsB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player or team.
    n = winsA + winsB
    print('\nGames simulated:', n)
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

if __name__== '__main__' : main()