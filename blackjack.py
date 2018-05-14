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
        if card[0] == 'Ace':
            self.aces += 1
        self.value += values[card[0]]

    def adjust_for_ace(self):
        while True:
            if self.aces > 0:
                if self.value > 21:
                    self.value += -10
                    self.aces += -1
                    print("Ace now equals 1")
            else:
                break

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total = self.total+self.bet

    def lose_bet(self):
        self.total = self.total-self.bet

def take_bet():
    while True:
        try:
            player_chips.bet=int(input("How much do you want to bet?"))
            if player_chips.bet > player_chips.total:
                raise SystemError('ISF')
            break
        except SystemError:
            print("You can't bet more than you have!")
        except ValueError:
            print("Please enter a vaild number.")


def hit(deck,hand):
    hand.add_card(deck.deal())


def hit_or_stand(deck,hand):

    if hand == 'player_hand':
        while True:
            hit_stand= input("Would you like to Hit or Stand? (enter Hit or Stand)")
            if hit_stand == "Hit":
                hit(deck, player_hand)
            elif hit_stand == "Stand":
                break
            else:
                print("Please enter either Hit or Stand")
            show_all(player_hand.cards,dealer_hand.cards)
            player_busts()
    else:
        while True:
            if dealer_hand.value < 17:
                hit(deck, dealer_hand)
                dealer_busts()
            else:
                break

def show_some(player,dealer):

    print("Dealer is showing")
    print(Card(dealer_hand.cards[1]))

def show_all(player,dealer):

    print("You have:")
    for card in player:
        print(Card(card))
    print("Current total " + str(player_hand.value))

def player_busts():
    if player_hand.value > 21:
        print("Bust!")
        player_chips.lose_bet()

def player_wins():
    if player_hand.value <= 21 and dealer_hand.value <= 21:
        if player_hand.value > dealer_hand.value:
            print('You win!')
            player_chips.win_bet()

def dealer_busts():
    if dealer_hand.value > 21:
        print("Dealer Bust!")
        player_chips.win_bet()

def dealer_wins():
    if dealer_hand.value <= 21 and player_hand.value <= 21:
        if dealer_hand.value > player_hand.value:
            print('You lost!')
            player_chips.lose_bet()

def push():
    if dealer_hand.value == player_hand.value:
        print("Tie!")

print("Welecome to Blackjack")
player_chips = Chips()
while True:
    print("Shuffling and dealing cards")
    playing_deck = Deck(suits,ranks)
    playing_deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())
    take_bet()
    show_some(player_hand.cards,dealer_hand.cards)
    show_all(player_hand.cards,dealer_hand.cards)
    while playing:
        hit_or_stand(playing_deck,player_hand)
        hit_or_stand(playing_deck,dealer_hand)
        break
    player.wins()
    dealer.wins()
    print("You now have " + str(player_chips.total) + " chips")
    while True:
        play_again=input("Do you want to play again?(Yes/No)")
        if  play_again== "No":
            break
        elif play_again== "Yes":
            break
        else:
            print("Please enter either Yes or No")
