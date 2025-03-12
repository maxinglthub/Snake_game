import turtle
import time

wn = turtle.Screen()
wn.setup(600, 600)
wn.tracer(0)


t1 = turtle.Turtle()
t1.shape('square')
t1.color('red')

t2 = turtle.Turtle()
t2.shape('square')
t2.color('blue')

t3 = turtle.Turtle()
t3.shape('square')
t3.color('green')

t4 = turtle.Turtle()
t4.shape('square')

t1.goto(0, 0)

while True:
    wn.update()

    t1.goto(t1.xcor() + 20, t1.ycor())
    time.sleep(0.1)
    t2.goto(t1.xcor() - 20, t2.ycor())
    time.sleep(0.1)
    t3.goto(t2.xcor() - 20, t3.ycor())
    time.sleep(0.1)
    t4.goto(t3.xcor() - 20, t4.ycor())
    time.sleep(0.1)
        
    

