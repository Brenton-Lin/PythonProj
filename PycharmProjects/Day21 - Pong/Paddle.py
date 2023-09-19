from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):

    def __init__(self, start_x, start_y):
        super().__init__()

        x_pos = start_x
        y_pos = start_y

        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.goto(x_pos, y_pos)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        pass

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
        pass
