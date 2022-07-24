import turtle

pen = turtle.Turtle()
screen = turtle.getscreen()

list1 = ["purple","red","orange","blue","green"]
turtle.bgcolor("black") 
for i in range(200):
    pen.speed(0)#make pen fast
    pen.color(list1[i%5])#to select different colour from the list
    pen.pensize(i/10)# pen not to go overboard
    pen.forward(i) #move forward
    pen.left(59) # turn pen to angle 59 (p)

