import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
deck=[]

class Card:

    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank

    def __str__(self):
        return self.rank+ ' of ' +self.suit

class Deck:
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))


    def __str__(self):
        card_string = ""
        for card in self.deck:
            card_string +='\n'+ card.__str__()
        return card_string


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        delt_card = self.deck.pop()
        return delt_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        if card.rank == 'Ace':
            self.aces += 1
        self.value += values[card.rank]

    def adjust_for_ace(self):
        while True:
            if self.aces > 0:
                if self.value > 21:
                    self.value += -10
                    self.aces += -1
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
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        hit_stand= input("\nWould you like to Hit or Stand? (enter h or s)")
        if hit_stand[0].lower() == "h":
            hit(deck, hand)
        elif hit_stand[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("\nPlease enter either h or s")
            continue
        break



def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts():
    print("Player busts!")
    player_chips.lose_bet()

def player_wins():
    if player_hand.value <= 21 and dealer_hand.value <= 21:
        if player_hand.value > dealer_hand.value:
            print('You win!')
            player_chips.win_bet()

def dealer_busts():
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
    playing_deck = Deck()
    playing_deck.shuffle()
    player_hand = Hand()
    player_hand.add_card(playing_deck.deal())
    player_hand.add_card(playing_deck.deal())
    dealer_hand = Hand()
    dealer_hand.add_card(playing_deck.deal())
    dealer_hand.add_card(playing_deck.deal())
    take_bet()
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(playing_deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(playing_deck,dealer_hand)
        show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts()
        else:
            player_wins()
            dealer_wins()
            push()

    print("You now have " + str(player_chips.total) + " chips")
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
