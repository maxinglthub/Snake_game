import turtle
import time

wn = turtle.Screen()
wn.setup(600, 600)

t = turtle.Turtle()
t.shape('square')
t.color('red')

alist = []
alist.append(t)

count = 0
while count < 3:
    t = turtle.Turtle()
    t.shape('square')
    alist.append(t)
    count = count + 1



while True:
    wn.update()
    time.sleep(1)
    
    alist[3].goto(alist[2].xcor(), alist[2].ycor())
    alist[2].goto(alist[1].xcor(), alist[1].ycor())
    alist[1].goto(alist[0].xcor(), alist[1].ycor())
    
    if count < 3:
        alist[0].goto(alist[0].xcor() + 20, alist[0].ycor())
        if alist[0].xcor() > 280:
            alist[0].goto(-280, alist[0].ycor())
        else:
            alist[0].goto(alist[0].xcor(), alist[0].ycor() + 20)
            
    count = count + 1