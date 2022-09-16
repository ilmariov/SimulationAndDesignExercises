from random import randint, random

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
    the point when serving. The one who serves first is chosen ramdomly.
    ''')
    
def getInputs():
    a = float(input('\nWhat is the prob. player or team A wins a serve? '))
    b = float(input('What is the prob. player or team B wins a serve? '))
    n = int(input('How many games to simulate? '))
    return a, b, n

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

def simOneMatch(probA, probB):
    setsA = 0
    setsB = 0
    while not matchOver(setsA, setsB):
        if setsA==0 and setsB==0:
            serving = whoServes()
            gameA, gameB, serving = simOneSet(serving, probA, probB)
            if gameA > gameB:
                setsA = setsA + 1
            else:
                setsB = setsB + 1
        else:
            gameA, gameB, serving = simOneSet(serving, probA, probB)
            if gameA > gameB:
                setsA = setsA + 1
            else:
                setsB = setsB + 1
    return setsA, setsB

def simOneSet(serving, probA, probB):
    wonGamesA = 0
    wonGamesB = 0
    while not setOver(wonGamesA, wonGamesB):
        scoreA, scoreB, serving = simOneGame(serving, probA, probB)   
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

def gameOver(a, b):
    # a and b represents scores for a tennis game
    # Returns True if the game is over, False otherwise.
    return (a>=4 or b>=4) and abs(a-b)>=2

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

def matchOver(a, b):
    # a and b represents sets won in a tennis match
    # Returns True if the match is over, False otherwise.
    return (a>=2 or b>=2) and abs(a-b)>=1
    
def whoServes():
    num = randint(0,1)
    if num == 0:
        serving = 'A'
    else:
        serving = 'B'
    return serving

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player or team.
    n = winsA + winsB
    print('\nGames simulated:', n)
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))

if __name__== '__main__' : main()