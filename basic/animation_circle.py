import turtle
turtle.bgcolor("black")
animation_circle = turtle.Screen()
animation_circle.title("Animation Circle ")
turtle=turtle.Turtle()
turtle.color("red")
turtle.speed(0)
turtle.hideturtle()
for i in range(100):
    turtle.circle(i)
    turtle._rotate(5)