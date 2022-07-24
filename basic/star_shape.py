# import turtle library------------------------------------
import turtle

# create the turtle screen using an object---------------------------
screen = turtle.getscreen()

# create the turtle pen--------------------------------------------
pen = turtle.Turtle()

turtle.bgcolor("black")

pen.color('red', 'yellow')
pen.begin_fill()
while True:
    pen.forward(200)
    pen.left(170)
    if abs(pen.pos()) < 1:
        break
pen.end_fill()
