import turtle

pen = turtle.Turtle()
#turtle.screensize(1100,1100)
turtle.title("National Flag Of Nigeria")

#draw a coloured rectangle
def rectangle(color):
    pen.begin_fill()
    pen.fillcolor(color)
    for i in range(2):
        pen.forward(300)
        pen.right(90)
        pen.forward(100)
        pen.right(90)
    pen.end_fill()

#draw the pole
pen.up()
pen.pensize(4)
pen.goto(0,-300)
pen.down()
pen.goto(0,300)

#Draw uppermost green
rectangle("Green")

#Draw white part
pen.right(90)
pen.forward(100)
pen.left(90)
rectangle("white")

#draw the green part
pen.right(90)
pen.forward(100)
pen.left(90)
rectangle("green")

pen.hideturtle()

