#Pls check link below if code have any proplems :)
#https://github.com/maxinglthub/Snake_game.git

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

snake = [t]
count = 0
while count < 3:
    count = count + 1
    p = turtle.Turtle()
    p.shape('square')
    p.penup()
    p.color('red')
    p.goto(-20*count, 0)
    snake.append(p)

wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

score = 0
speed = 3
level = 0
direction = 0 #right

apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))
while apple.xcor() == p.xcor() and apple.ycor() == p.ycor():
    apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))

stop = False

while not stop:
    wn.update()
    wn.tracer(0)
    time.sleep(0.1)
    t.speed(speed)

    if t.xcor() == apple.xcor() and t.ycor() == apple.ycor():
        print("Last apple at: ", apple.xcor(), apple.ycor())
        score = score + 1
        if level == 10 or level == "Maxlevel":
            level = "Maxlevel"
        else: 
            level = level + 1
        apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))
        while apple.xcor() == p.xcor() and apple.ycor() == p.ycor():
            apple.goto(20*random.randint(-14, 14), 20*random.randint(-14, 14))
        
        p = turtle.Turtle()
        p.shape('square')
        p.penup()
        p.color('red')
        snake.append(p)

        print("Now apple at: ", apple.xcor(), apple.ycor())
        print("Score: ", score)
        print("Your level: ", level)
        print("------------------")
        speed = speed + 0.5

    i = len(snake) - 1
    while i > 0:
        snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())
        i = i - 1

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
        
    i = len(snake) - 1
    while i > 0:
        if t.xcor() == snake[i].xcor() and t.ycor() == snake[i].ycor():
            stop = True
        i = i - 1

print("------Game over------")
print("Your score: ", score)
print("Your level: ", level)
print("GG")
print("---------------------")
