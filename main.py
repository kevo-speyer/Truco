import random
import config
from copy import copy
random.seed()

def run():
    """ Primer Intento de programar un Truco"""
    
    # Enter player name
    #player_name = raw_input("Put your Name: \n ")
    player1 = Player(raw_input("Put Player 1 name: \n "))
    player2 = Player(raw_input("Put Player 2 name: \n ")) 
    
    # Generate Deck
    cards = gen_deck()
        
    game_on = True
    start_pl = 0
    while game_on == True :
        deck = copy(cards) # Cards being played this hand
        deal_cards(deck, player1, player2)
        
        play_set(player1, player2, start_pl) 

        game_on = check_score(player1, player2, game_on)

def play_set(pl1, pl2, start):
    """ play hand of 3 cards"""
    for plyr in pl1, pl2:
        print "Cards of ", plyr.name, " are :"
        for this_card in plyr.hand:
            print this_card.num, this_card.suit 
            
    pl1.score += 1

def check_score(pl1, pl2, game_on):
    """Check if a player has obtained 30 points"""
    for ply in pl1, pl2:
        if ply.score >= 30:
            game_on = False            
            print "Player ", ply.name, " won the game with ", ply.score, " points."
    return game_on

def deal_cards(deck,pl1,pl2):
    """ Give 3 cards to each player """
    n_cards = 40
    for plyr in pl1, pl2:
        hand = []
        for i in range(3):            
            new_card_numb = random.randint(0, n_cards-1)         
            hand.append( deck[new_card_numb] )            
            deck.pop(new_card_numb) 
            n_cards -= 1

        plyr.set_hand( hand ) 

    return pl1, pl2

def run_set(deck,pl1,pl2):
    """Play 3 cards"""
   
def gen_deck():
    """ generate random card"""
    deck = [] 
    for suit in config.palos:
        for number in range(1,11):
            new_card = Card(number, suit)            
            deck.append(new_card)
    return deck

class Card:
    """"Card"""
    def __init__(self, number, suit):
        self.num = number
        self.suit = suit
    
class Player:
    """ Object Player"""
    def __init__(self, name, points=0):
        self.name = name
        self.score = points
 
    def set_hand(self, hand):
        """Recieve cards from the deck"""
        self.hand = hand
