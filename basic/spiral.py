import turtle

pen = turtle.Turtle()
screen = turtle.bgcolor()
turtle.bgcolor("black")

def spiral (distance , angle):
    if distance >0:
        pen.forward(distance)
        pen.right(angle)
        spiral(distance-5,angle)

pen.speed(0)
#pen.delay(0)
length =500
turn_by =121

pen.goto(-250,300)
pen.color("red")
spiral(length,turn_by)


