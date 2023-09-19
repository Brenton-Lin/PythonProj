from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # No need to generate a turtle, because we've inherited from the base turtle
        # we will spawn just like a regular turtle.

        self.penup()
        self.hideturtle()
        self.shape("circle")
        self.goto(0, 0)
        self.color("White")
        self.showturtle()
        self.speed = 10
        self.setheading(60)
        self.x_vel = 10
        self.y_vel = 10

    def move(self):
        new_x = self.xcor() + self.x_vel
        new_y = self.ycor() + self.y_vel
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_vel *= -1

    def paddle_bounce(self):
        self.x_vel *= -1

    def reset_pos(self):
        self.goto(0,0)
        self.x_vel *= -1
        pass
