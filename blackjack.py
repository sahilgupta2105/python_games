# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = "Hit or Stand?"
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        dum="Hand contains "
        for i in self.cards:
            dum= dum+ i.get_suit()+i.get_rank()+" "
        return dum

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        val=0
        for i in self.cards:
            if i.get_rank()=='A':
                if val+VALUES[i.get_rank()]+10 <=21:
                    val=val+VALUES[i.get_rank()]+10
                else:
                    val=val+VALUES[i.get_rank()]
            else:
                    val=val+VALUES[i.get_rank()]
        return val
   
    def draw(self, canvas, pos):
        dum1=1
        for i in self.cards:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(i.get_rank()), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(i.get_suit()))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0]*dum1+20 + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
            dum1=dum1+1
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards=[]
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i,j))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)
        
    def deal_card(self):
        c1= self.cards[0]
        self.cards.remove(c1)
        return c1
    
    def __str__(self):
        dum="Deck contains "
        for i in self.cards:
            dum= dum+ i.get_suit()+i.get_rank()+" "
        return dum



#define event handlers for buttons
def deal():
    global outcome, in_play, deck1, player_hand, dealer_hand,score
    
    if in_play:
        outcome= "You lost, New Deal?"
        score=score-1
    else:
        outcome= "Hit or Stand?"
        
    deck1=Deck()
    deck1.shuffle()
    player_hand=Hand()
    dealer_hand=Hand()
    player_hand.add_card(deck1.deal_card())
    player_hand.add_card(deck1.deal_card())
    dealer_hand.add_card(deck1.deal_card())
    dealer_hand.add_card(deck1.deal_card())
    in_play = True

def hit():
    global player_hand, deck1, outcome,score, in_play
    
    if player_hand.get_value()<=21:
        player_hand.add_card(deck1.deal_card())
        if player_hand.get_value()>21:
            outcome= "You have been busted. New Deal?"
            in_play=False
            score=score-1
       
def stand():
   
    global player_hand, dealer_hand,outcome,score, in_play
    print player_hand.get_value()
    if(player_hand.get_value()>21):
        in_play=False
        outcome="You have been busted!!! New Deal?"
    else:
        val=dealer_hand.get_value()
        while val<17:
            dealer_hand.add_card(deck1.deal_card())
            val=dealer_hand.get_value()
        val=dealer_hand.get_value()
        if val>21:
            in_play=False
            outcome="Dealer is busted. New Deal?"
            score=score+1
        elif val>=player_hand.get_value():
            in_play=False
            outcome="Dealer won. New Deal?"
            score=score-1
        else:
            in_play=False
            outcome="You won. New Deal?"
            score=score+1
    print val
            
# draw handler    
def draw(canvas):
    
    global player_hand, dealer_hand, outcome, in_play, score
    
    dealer_hand.draw(canvas,[50,200])
    if in_play:
        canvas.draw_image(card_back,(CARD_CENTER[0],CARD_CENTER[1]),CARD_SIZE,(50+ CARD_CENTER[0], 200 + CARD_CENTER[1]),CARD_SIZE)
        
        
    
    player_hand.draw(canvas,[50,400])
    canvas.draw_text(outcome,[200,50],25,'Blue')
    canvas.draw_text("Dealer",[50,170],22,'Blue')
    canvas.draw_text("Player",[50,370],22,'Blue')
    canvas.draw_text("Score: "+str(score),[300,200],22,'Blue')
    canvas.draw_text("BlackJack",[50,50],26,'Blue')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
