import random

'''
This is a blackjack game in the command line
'''
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True

#create deck
class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck():

    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    #Shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():

    def __init__(self):
        self.cards = [] #Start with no cards in hand
        self.value = 0 #no cards so no value
        self.aces = 0 #will need to keep track of aces if we need to change from 11 to 1

    def add_card(self, card):
        self.cards.append(card) #adds a card to hand
        self.value += values[card.rank] #Adds value of the card in hand to value to keep track of 21

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while  self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win(self):
        self.total += self.bet

    def lose(self):
        self.total -= self.bet
#Bet
def bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you do not have enough chips! you have: {}'.format(chips.total))
            else:
                break


#Player action
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stay(deck,hand):
    global playing

    while True:
        x = input('Hit or Stand?  Enter h or s ')
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print('Player stays.  Dealer\'s turn')
            playing = False
        else:
            print('Sorry.  I did not understand that.  Please enter h or s only')
            continue
    break

def player_busts(player, dealer, chips):
    print('Bust.  You lose')
    chips.lose()

def player_wins(player, dealer, chips):
    print('You win!')
    chips.win()

def dealer_busts(player, dealer, chips):
    print('The dealer busted.  You win!')
    chips.win()

def dealer_wins(player, dealer, chips):
    print('Dealer wins, you lose')
    chips.lose

def push(player, dealer):
    print('Dealer and player tie.  Push')





test_deck = Deck()
test_deck.shuffle()

test_player = Hand()

#deal 1 card
pulled_card = test_deck.deal()

print(pulled_card)

test_player.add_card(pulled_card)

print(test_player.value)

print(test_deck)
