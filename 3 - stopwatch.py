# template for "Stopwatch: The Game"
import simplegui
import math

# define global variables
t = 0
total = 0
success = 0
D = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global D
    A = int(math.floor(t / 600))
    B = int(math.floor((t % 600) / 100))
    
    if B > 0:
        C = int(math.floor(t % 600) - B*100)/10
    elif B == 0:
        C = int(math.floor(t % 600 / 10))
    
    D = int(t % 600 % 10)
    return str(A)+":"+str(B)+str(C)+"."+str(D)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total, success, D
    timer.stop()
    total += 1
    if D == 0 :
        success += 1

def reset():
    global t
    t = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t = t + 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),[65, 100], 24, "White")
    canvas.draw_text(str(success)+"/"+str(total),[150,30], 24, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()


# Please remember to review the grading rubric
