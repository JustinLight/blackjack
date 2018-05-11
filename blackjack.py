import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
deck=[]

class Card:

    def __init__(self,card):
        self.suit=card[1]
        self.rank=card[0]

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:
    def __init__(self,suits,ranks):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append((rank,suit))


    def __str__(self):
        card_string = ""
        for card in self.deck:
            card_string += card[0]+" of " +card[1] + "\n"
        return(card_string)


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        delt_card = self.deck.pop(0)
        return delt_card

class Hand(Card):
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        Card.__init__(self,card)
        self.cards.append(card)
        print(self.cards)
        if card[0] == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        pass

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total+self.bet

    def lose_bet(self):
        self.total = self.total-self.bet

def take_bet():
    #self.bet()=int(input("How much do you want to bet?"))
    pass

def hit(deck,hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck,hand):
    global playing

    pass

def show_some(player,dealer):

    pass

def show_all(player,dealer):

    pass

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass

def dealer_wins():
    pass

def push():
    pass

test_deck = Deck(suits,ranks)
print(test_deck)
test_deck.shuffle()
print(test_deck)
player_hand=Hand()
player_hand.add_card(test_deck.deal())
print(player_hand)
player_hand.add_card(test_deck.deal())
print(player_hand)
dealer_hand=Hand()
dealer_hand.add_card(test_deck.deal())
print(dealer_hand)
dealer_hand.add_card(test_deck.deal())
print(dealer_hand)
