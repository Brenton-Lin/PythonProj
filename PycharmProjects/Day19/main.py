from turtle import Turtle, Screen
import random
todd = Turtle()
todd.hideturtle()
screen = Screen()


def forward():
    todd.forward(10)


def backward():
    todd.back(10)


def left():
    new = todd.heading() + 10
    todd.setheading(new)


def right():
    new = todd.heading() - 10
    todd.setheading(new)


def etch_sketch():
    todd.showturtle()
    screen.onkeypress(forward, "w")
    screen.onkeypress(backward, "s")
    screen.onkeypress(left, "a")
    screen.onkeypress(right, "d")
    screen.listen()
    screen.exitonclick()


def turtle_race():
    """Multiple instances of turtles, each with their own states"""
    colors = ["red", "blue", "green", "purple"]
    screen.setup(width=600, height=600)
    turtles = []

    '''turtle creation'''
    for index in range(0,4):
        turt = Turtle(shape="turtle")
        turt.color(colors[index])
        turt.penup()
        turtles.append(turt)

    starting_line = -300
    set_start(turtles, starting_line)

    user_choice = screen.textinput(title="Choose Your Turtle!", prompt="Who will win? Pick a color: ")
    winner = go(turtles)

    if winner == user_choice:
        print("winner!")
    else:
        print("loser!")
    screen.exitonclick()


def go(turtles):
    race_won = False
    while not race_won:
        for turtle in turtles:
            turtle.forward(random.randint(1,15))
            if turtle.xcor() >= 270:
                race_won = True
                return turtle.pencolor()


def set_start(turtles, starting_x):
    places = len(turtles)
    delta_y = screen.canvheight/places
    start_y = screen.canvheight/2*-1 + 50
    for turtle in turtles:
        turtle.shapesize(2,2)
        turtle.hideturtle()
        turtle.setpos(starting_x, start_y)
        turtle.showturtle()

        start_y += delta_y



'''Functions may be passed in python as the func type, without parenthesis'''

turtle_race()