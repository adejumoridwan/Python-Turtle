# Setting up the game environment
#--------------------------------------------
import turtle
import random

#Create the two turtles that will correspond to different palyers
#------------------------------------------------------------------------
#Player 1
player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)

#Player 2
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

#Create the turtles home
#--------------------------------
#Player 1 home
player_one.goto(200,60)
player_one.pendown()
player_one.circle(40)
player_one.penup()
player_one.goto(-200,100)

#Player 2 home
player_two.goto(200,-140)
player_two.pendown()
player_two.circle(40)
player_two.penup()
player_two.goto(-200,-100)

#Create a virtual die for the game
#----------------------------------
die = [1,2,3,4,5,6]

for i in range(20):
    if player_one.pos() >= (200,0):
        print("Player One Wins!")
        break
    elif player_two.pos() >= (200,0):
        print("Player Two Wins!")
        break
    else:
        #for player one
        player_one_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The result of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_one.fd(20*die_outcome)
        #for player two
        player_two_turn = input("Press 'Enter' to roll the die")
        die_outcome = random.choice(die)
        print("The resutlt of the die roll is: ")
        print(die_outcome)
        print("The number of steps will be: ")
        print(20*die_outcome)
        player_two.fd(20*die_outcome)
