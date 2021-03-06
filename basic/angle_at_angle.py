"""
Steps
- First Import turtle
- Create the Python screen
- Create the Python turtle Pen
- Draw a line for a specified angle e.g 0 degrees
- Draw a line for a line for angles 0-360 degrees

"""


import turtle

screen = turtle.getscreen()
pen = turtle.Turtle()

for angle in range(0, 360, 5):
    pen.setheading(angle)
    pen.forward(100)
    pen.write(str(angle) + '😎')
    pen.backward(100)

