from random import randint

def main():
    printIntro()
    n = int(input('\nHow many games to simulate? '))
    busts = simNGames(n)
    printProb(n, busts)

def printIntro():
    print('''
    This program simulates multiple games of blackjack and estimates
    the probability that the dealer will bust when starting with one
    specific card showing.
    ''')

def simNGames(n):
    busts = [0]*10
    for i in range(n):
        checker,dcard1 = simOneGame()
        for j in range(10):
            if checker:
                if dcard1 == j+1:
                    busts[j] = int(busts[j]) + 1
    return busts

def simOneGame():
    # This function checks if the dealer bust or not
    # it prints True if he busts, False otherwise.
    checker = False
    pcard1, pcard2, dcard1, dcard2 = deal()
    player_hand = hit(pcard1, pcard2)
    dealer_hand = hit(dcard1, dcard2)
    if player_hand==21 or dealer_hand==21:
        checker = False
    elif (player_hand > dealer_hand):
        last_dcard = randint(1,10)
        if dealer_hand + last_dcard > 21:
            checker = True
    else:
        while (player_hand <= dealer_hand) and (player_hand < 21) and (dealer_hand < 21):
            last_pcard = randint(1,10)
            player_hand = player_hand + last_pcard
            if player_hand < 21:
                last_dcard = randint(1,10)
                dealer_hand = dealer_hand + last_dcard
                if dealer_hand > 21:
                    checker = True
    return checker, dcard1

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
        new_card = 0
        while ((hand - new_card < 17) or (hand - new_card >= 21)):
            hand, new_card = getClose(cards, hand)
        hand = hand - new_card
    else:
        hand = hand + 10
    return hand

def getClose(cards,hand):
    switch = 0
    new_card = randint(1,10)
    while (hand < 21):
        new_card = randint(1,10)
        cards.append(new_card)
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
    return hand, new_card

def blackjack(c1, c2):
    return ((c1==1 and c2==10) or (c1==10 and c2==1))

def hasAce(cards):
    checker = None
    for i in range(len(cards)):
        if int(cards[i]) == 1:
            checker = True
            break
    return checker

def printProb(n, busts):
    print('\nAfter simulating {} games of blackjack, the estimated probability'.format(n))
    print('that the dealer will bust when showing one specific initial card is:')
    print('')
    for i in range(10):
        print('Card: {0:02d} ---- Probability: {1:0.1%}'.format(i+1, int(busts[i])/n))


if __name__=='__main__' : main()