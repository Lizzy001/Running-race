# from turtle import Turtle, Screen
#
# lizzy = Turtle()
# screen = Screen()
#
# def move_forwards():
#     lizzy.forward(10)
#
# def move_backwards():
#     lizzy.backward(10)
#
#
# def turn_left():
#     new_heading = lizzy.heading() + 10
#     lizzy.setheading(new_heading)
#
#
# def turn_right():
#     new_heading = lizzy.heading() - 10
#     lizzy.setheading(new_heading)
#
# def clear():
#     lizzy.clear()
#     lizzy.penup()
#     lizzy.home()
#     lizzy.clear()
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")
#
# screen.exitonclick()

# ###################################################

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Play your game", prompt="Which turtle will win the race! Enter color:")
colours = ("yellow", "green", "purple", "blue", "orange", "red")
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()