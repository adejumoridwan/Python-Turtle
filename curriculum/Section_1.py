# import turtle library------------------------------------
import turtle

# create the turtle screen using an object---------------------------
s = turtle.getscreen()

# create the turtle pen--------------------------------------------
t = turtle.Turtle()

# turtle movement---------------------------------------------------
# move the turtle to the forward
t.forward(100)

# move the turtle to backward
t.backward()

# move the turtle to the right
t.right(90)

# move the turtle to the left
t.left(90)

#they can be alternatively written as
t.fd()
t.bk()
t.rt()
t.lt()

# go to a new screen position and reset turtle------------------------
t.goto(122,222)
t.home()

# draw a circle----------------------------------------
t.circle()

# draw a dot----------------------------------------------
t.dot()

# change the screen colour---------------------------------
turtle.bgcolor()

# change the screen title---------------------------------
turtle.title()

# change the turtle size--------------------------------
t.shapesize()

# changing the pen size(line thichness)-----------------------------------
t.pensize(0)
t.forward(30)

# changing turtle and pen color--------------------------------------
# change the fill color
t.fillcolor()

# change the pen color
t.pencolor()

#change both fill and pen color
t.color("green","yellow")

# Do want to draw an image?----------------------------
t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(100)
t.end_fill()

#Changing the turtle shape----------------------------
t.shape("turtle")
t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("circle")
t.shape("turtle")
t.shape("tiangle")
t.shape("classic")

#Changing the pen speed--------------------------------------
t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)

#Changing all your turtle settings in one line----------------------------
#Longer method
t.pencolor("purple")
t.fillcolor("orange")
t.pensize(10)
t.speed(9)
t.begin_fill()
t.circle(90)
t.end_fill()

#ShortCut Method
t.pen(pencolor = "purple", fillcolor = "orange", pensize = 10, speed = 9)
t.begin_fill()
t.circle()
t.end_fill()

#changing the position of your pen without drawing------------------------------------
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.rt(90)
t.pendown()
t.fd(100)
t.rt(90)
t.penup()
t.fd(100)
t.pendown()

#undoing changes------------------------------
t.undo()

#clearing the screen-----------------------------
t.clear()

#reset the environment
t.reset()

#Leaving a stamp of the turtle on the screen(footprint)-----------------------------
t.stamp()
t.fd(100)
t.stamp()
t.fd(100)

#Clear stamp--------------------------------------
t.clearstamp(8)

#Cloning your turtle------------------------------------------
c = t.clone()
t.color("magenta")
c.color("red")
t.circle(100)
c.circle(60)










turtle.title("My Turtle ")

t.shapesize(1,5,10)
t.shapesize(1,1,1)

t.pensize(4)

t.forward(100)

t.shapesize(1.5,1.5,1.5)

t.fillcolor("black")

t.pencolor("black")

t.color("green", "red")

t.color("")

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

t.shape("turtle")
t.shape("arrow")
t.shape("turtle")

t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)

