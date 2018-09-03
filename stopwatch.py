# template for "Stopwatch: The Game"
import simplegui
# define global variables
time_global=0
run=False
x=0
y=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min=t/600
    mil_sec=t%10
    sec1=((t-mil_sec)/10)%10
    sec2=((t-min-sec1-mil_sec)/100)%6
    return str(min)+":"+str(sec2)+str(sec1)+"."+str(mil_sec)
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global run
    timer.start()
    run = True
    
def stop():
    timer.stop()
    global run, x, y, time_global
    if run:
        run=False
        y=y+1
        if not time_global%10:
            x=x+1
    
def reset():
    global time_global, x, y
    time_global=0
    timer.stop()
    x=0
    y=0
    
# define event handler for timer with 0.1 sec interval

def tick():
    global time_global
    time_global=time_global+1
    
# define draw handler
def draw_handler(canvas):
    global time_global
    canvas.draw_text(format(time_global),[105,165],40,'Red')
    canvas.draw_text(str(x)+"/"+str(y),[240,50],30,'Green')
        
    
# create frame
frame= simplegui.create_frame('Timer',300,300)
frame.set_canvas_background('White')
frame.add_button('Start',start,150)
frame.add_button('Stop',stop,150)
frame.add_button('Reset',reset,150)
timer= simplegui.create_timer(100,tick)

# register event handlers
frame.set_draw_handler(draw_handler)

# start frame
frame.start()


# Please remember to review the grading rubric
