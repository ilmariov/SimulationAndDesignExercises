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
    # checker = None
    pcard1, pcard2, dcard1, dcard2 = deal()
    print(pcard1, pcard2)
    player_hand = hit(pcard1, pcard2)
    print(player_hand)
    print('-------------------------')
    print(dcard1, dcard2)
    dealer_hand = hit(dcard1, dcard2)
    print(dealer_hand)

def hasAce(card1, card2):
    return (card1==1 or card2==1)

def hasAce2(cards):
    checker = None
    for i in range(len(cards)):
        if int(cards[i]) == 1:
            checker = True
            break
    return checker

def blackjack(c1, c2):
    return ((c1==1 and c2==10) or (c1==10 and c2==1))

def deal():
    pcard1 = randint(1,10)
    pcard2 = randint(1,10)
    dcard1 = randint(1,10)
    dcard2 = randint(1,10)
    return pcard1, pcard2, dcard1, dcard2

'''def firstHand():
    # returns 1:player wins, 2:dealer wins, 3:game continues, 4:are even
    pcard1, pcard2, dcard1, dcard2 = deal()
    player_hand = pcard1 + pcard2
    dealer_hand = dcard1 + dcard2
    if hasAce(pcard1, pcard2) or hasAce(dcard1, dcard2):
        if hasAce(pcard1, pcard2) and player_hand==11:
            if hasAce(dcard1, dcard2) and dealer_hand==11:
                return 4
            else:
                return 1
        elif '''
        
def hit(card1, card2):
    hand = card1 + card2
    cards = [card1, card2]    
    if not blackjack(card1, card2):
        while (hand < 21):
            new_card = randint(1,10)
            cards.append(new_card)
            print(new_card)
            if (hasAce2(cards) and (7 <= hand <= 11)):
                hand = hand + new_card + 10
                if hand > 21:
                    hand = hand -10
            else:
                hand = hand + new_card
    else:
        hand = hand + 10
    return hand


if __name__=='__main__' : simOneGame()
