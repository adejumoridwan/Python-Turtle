import turtle
corona = turtle.Turtle()
s=turtle.Screen()
turtle.screensize(1400,1400)
corona.pencolor("red")
corona.write("Stay Home Stay Safe ",'false','center',font=('Showcard gothic',40))
s.bgcolor("black")
corona.pencolor("dark green")
corona.pensize(2)
Python=0
CplusPlus=0
corona.speed(0)
corona.penup()
corona.goto(0,250)
corona.pendown()
while True:
    corona.forward(Python)
    corona.right(CplusPlus)
    Python+=3
    CplusPlus+=1
    if CplusPlus==210:
        break
    corona.hideturtle()
turtle.done()