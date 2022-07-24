import turtle

pen = turtle.Turtle()
screen = turtle.Screen()

#turtle.screensize(1400,1400)
screen.bgcolor("black")
pen.pencolor("dark green")
pen.pensize(2)

Distance=0
Angle=0

pen.speed(0)
pen.penup()
pen.goto(0,250)
pen.pendown()

while True:
    pen.forward(Distance)
    pen.right(Angle)
    Distance+=3
    Angle+=1
    if Angle==210:
        break
    #pen.hideturtle()


pen.pencolor("red")
pen.write("Stay Home Stay Safe ",'false','center',font=('Showcard gothic',40))

