import turtle
import time
import random

def move_up():  
    global direction
    if direction != 1:
        direction = 1

def move_down():
    global direction
    if direction != 3:
        direction = 3

def move_left():
    global direction
    if direction != 2:
        direction = 2

def move_right():
    global direction
    if direction != 0:
        direction = 0

wn = turtle.Screen()
wn.setup(600, 600)

t = turtle.Turtle()
t.penup()
t.shape('square')
t.color('red')

apple = turtle.Turtle()
apple.shape('square')
apple.penup()
apple.color('green')

wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

score = 0

direction = 0 #right

apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))

while True:
    wn.update()
    wn.tracer(0)
    time.sleep(0.1)

    if direction == 0:  #right
        t.goto(t.xcor() + 20, t.ycor())
        if t.xcor() > 280:
            t.goto(-280, t.ycor())
    elif direction == 1: #up
        t.goto(t.xcor(), t.ycor() + 20)
        if t.ycor() > 280:
            t.goto(t.xcor(), -280)
    elif direction == 2: #left
        t.goto(t.xcor() - 20, t.ycor())
        if t.xcor() < -280:
            t.goto(280, t.ycor())
    elif direction == 3: #down
        t.goto(t.xcor(), t.ycor() - 20)
        if t.ycor() < -280:
            t.goto(t.xcor(), 280)
    
    if t.xcor() == apple.xcor() and t.ycor() == apple.ycor():
        score = score + 1
        apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))

    print(score)