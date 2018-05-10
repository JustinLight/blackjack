import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
deck=[]

class Deck:
    def __init__(self,suits,ranks):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append((rank,suit))

    def __str__(self):
        pass

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        Hand.add_card(deck.pop(0))

class Hand:
    def __init__(self,card):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        if card[1] == 'Ace':
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
    Chips.self.bet()=int(input("How much do you want to bet?"))

def hit(deck,hand):

    pass

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

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
