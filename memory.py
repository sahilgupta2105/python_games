# implementation of card game - Memory

import simplegui
import random

CARD_X=25
CARD_Y=50

counter=0
state=0
card1=10
card2=10
exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
num_lst=range(8)
num_lst.extend(range(8))
random.shuffle(num_lst)
#print exposed

# helper function to initialize globals
def new_game():
    global counter,state,card1,card2,exposed,num_lst
    exposed=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    num_lst=range(8)
    num_lst.extend(range(8))
    random.shuffle(num_lst)
    counter=0
    state=0
    card1=10
    card2=10

     
# define event handlers
def mouseclick(pos):
    # card number which is clicked
    loc_x=pos[0]//50
    global exposed,counter
    global state,card1,card2
    if state==0:
        state=1
        exposed[loc_x]=True
        card1=loc_x
    elif state==1:
        if not loc_x==card1:
            state=2
            exposed[loc_x]=True
            card2=loc_x
    else:
        if not num_lst[card1]==num_lst[card2]:
            exposed[card1]=False
            exposed[card2]=False
            counter+=1
        state=1
        exposed[loc_x]=True
        card1=loc_x
       


    
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #Variable to track location in num_lst
    it=0
    global counter
    label.set_text("Turns = "+str(counter))
    #Loop for drawing the cards
    for i in num_lst:
        xx=CARD_X+it*50
        yy=CARD_Y
        # the statement checks if the card should be exposed or not
        if exposed[it]:
            canvas.draw_text(str(i),(xx,yy),32,'Red')
        else:
            canvas.draw_polygon([(xx-25,yy-50),(xx+25,yy-50),(xx+25,yy+50),(xx-25,yy+50)],1,'Black','Green')
        it+=1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
