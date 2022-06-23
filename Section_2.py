#Using Loops and Conditional Statements-----------------------------
#------------------------------------------------------------------------------
#---Loops are a set of instructions that are continously repeated until a particular condition is satisfied
#---Conditional statements carry out a certain task based on a condtion that is satisfies
#---Indentations are used to define block of code, especially in loops and conditional statements

#for Loops ------------------------------
#Do you remember the that you had to create a square and repeated the same line of code 4 times like this:
#A faster way of doing it is to use the for loop


#let's import turtle and define the screen and turtle
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

for i in range(4):
    t.fd(100)
    t.rt(90)

#while loops---------------------------------------------
#unlike the for loop the while loop is used to perform a certain task while a condition is satisfied

n = 10
while n <= 100:
    t.circle(n)
    n = n+10

#conditional statements
u = input("Would you like me to draw a shape? Type yes or no: ")
if u == "yes":
    t.circle(50)

#among us