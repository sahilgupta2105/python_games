# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction==RIGHT:
        ball_vel=[random.randrange(5,8),-random.randrange(3,6)]
    else:
        ball_vel=[-random.randrange(5,8),-random.randrange(3,6)]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=[HALF_PAD_WIDTH,HALF_PAD_HEIGHT]
    paddle2_pos=[WIDTH-HALF_PAD_WIDTH,HALF_PAD_HEIGHT]
    paddle1_vel=0
    paddle2_vel=0
    score1=0
    score2=0
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_text(str(score1),[WIDTH/4,HEIGHT*0.1],20,'White')
    canvas.draw_text(str(score2),[3*WIDTH/4,HEIGHT*0.1],20,'White')
    # update ball
    if ball_pos[1]<BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    elif ball_pos[1]>HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    ball_pos[0]+=ball_vel[0]
    ball_pos[1]+=ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,10,'Red','Red')
    # update paddle's vertical position, keep paddle on the screen
    if not(paddle1_pos[1]+ paddle1_vel + HALF_PAD_HEIGHT>HEIGHT) and not(paddle1_pos[1]+ paddle1_vel - HALF_PAD_HEIGHT<0) :
        paddle1_pos[1]+=paddle1_vel
    
    if not(paddle2_pos[1]+ paddle2_vel + HALF_PAD_HEIGHT>HEIGHT) and not(paddle2_pos[1]+ paddle2_vel - HALF_PAD_HEIGHT<0) :
        paddle2_pos[1]+=paddle2_vel
    # draw paddles
    canvas.draw_polygon([[paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT],[paddle1_pos[0]-HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT],[paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT],[paddle1_pos[0]+HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT]],4,'Green','Green')
    canvas.draw_polygon([[paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT],[paddle2_pos[0]-HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],[paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT],[paddle2_pos[0]+HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT]],4,'Green','Green')
    # determine whether paddle and ball collide    
    if ball_pos[0]<PAD_WIDTH+BALL_RADIUS:
        if paddle1_pos[1]-HALF_PAD_HEIGHT<ball_pos[1]<paddle1_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0]=-1.1*ball_vel[0]
        else:
            score2+=1
            spawn_ball(RIGHT)
    elif ball_pos[0]>WIDTH-PAD_WIDTH-BALL_RADIUS:
        if paddle2_pos[1]-HALF_PAD_HEIGHT<ball_pos[1]<paddle2_pos[1]+HALF_PAD_HEIGHT:
            ball_vel[0]=-1.1*ball_vel[0]
        else:
            score1+=1
            spawn_ball(LEFT)
        
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP['w'] or key==simplegui.KEY_MAP['W']:
        paddle1_vel=-7
    elif key==simplegui.KEY_MAP['up']:
        paddle2_vel=-7
    elif key==simplegui.KEY_MAP['s'] or key==simplegui.KEY_MAP['S']:
        paddle1_vel=7
    elif key==simplegui.KEY_MAP['down']:
        paddle2_vel=7
    
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key==simplegui.KEY_MAP['w'] or key==simplegui.KEY_MAP['s'] or key==simplegui.KEY_MAP['S'] or key==simplegui.KEY_MAP['W']:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP['down'] or key==simplegui.KEY_MAP['up']:
        paddle2_vel=0

def restart():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button('Restart',restart,200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
