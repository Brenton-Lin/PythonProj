from turtle import Turtle
import random



class Fud(Turtle):
    class_attribute = "test"
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_pos = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(random_pos)


