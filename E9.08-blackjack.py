from random import randint

def main():
    printIntro()
    n = int(input('\nHow many games to simulate? '))
    busts = simNGames()
    printProb(n, busts)

def printIntro():
    print('''
    This program simulates multiple games of blackjack and estimates
    the probability that the dealer will bust.
    ''')

def simNGames(n):
    busts = 0
    for i in range(n):
        if simOneGame():
            busts = busts + 1
    return busts

def simOneGame():
    # This function checks if the dealer bust or not
    # it prints True if he busts, False otherwise.
    checker = False
    pcard1, pcard2, dcard1, dcard2 = deal()
    player_hand = hit(pcard1, pcard2)
    dealer_hand = hit(dcard1, dcard2)
    if player_hand == 21:
        checker = False
    elif dealer_hand > 21:
        checker = True
        if player_hand > 21:
            checker = False
    return checker

def deal():
    pcard1 = randint(1,10)
    pcard2 = randint(1,10)
    dcard1 = randint(1,10)
    dcard2 = randint(1,10)
    return pcard1, pcard2, dcard1, dcard2
    
def hit(card1, card2):
    hand = card1 + card2
    cards = [card1, card2]    
    if not blackjack(card1, card2):
        switch = 0
        while (hand < 21):
            new_card = randint(1,10)
            cards.append(new_card)
            print(new_card)
            if hasAce(cards):
                if hand <= 11:
                    hand = hand + new_card + 10
                    switch = 1
                    if hand > 21:
                        hand = hand - 10
                        switch = 0
                elif (switch==1 and (hand + new_card > 21)):
                    hand = hand + new_card -10
                    switch = 0
                else:
                    hand = hand + new_card
            else:
                hand = hand + new_card
    else:
        hand = hand + 10
    return hand

def blackjack(c1, c2):
    return ((c1==1 and c2==10) or (c1==10 and c2==1))

def hasAce(cards):
    checker = None
    for i in range(len(cards)):
        if int(cards[i]) == 1:
            checker = True
            break
    return checker


if __name__=='__main__' : simOneGame()