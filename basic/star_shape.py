# import turtle library------------------------------------
import turtle

# create the turtle screen using an object---------------------------
s = turtle.getscreen()

# create the turtle pen--------------------------------------------
t = turtle.Turtle()

t.color('red', 'yellow')
t.begin_fill()
while True:
    t.forward(200)
    t.left(170)
    if abs(t.pos()) < 1:
        break
t.end_fill()
t.done()


# import turtle library------------------------------------
import turtle

# create the turtle screen using an object---------------------------
s = turtle.getscreen()

# create the turtle pen--------------------------------------------
t = turtle.Turtle()

t.color('red', 'yellow')
t.begin_fill()
t.forward(200)
t.left(170)
t.end_fill()
t.done()