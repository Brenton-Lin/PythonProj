from turtle import Screen, Turtle


class Snake:
    segment_size = 1
    speed = 20

    def __init__(self, starting_segs):

        x_index = 0
        y_index = 0
        self.snake_segments = []

        for _ in range(starting_segs):
            self.add_segment(position=(x_index, y_index))
            x_index -= self.segment_size * 20

        self.head = self.snake_segments[0]

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[segment].goto(self.snake_segments[segment - 1].pos())

        self.head.forward(self.segment_size * self.speed)

    def add_segment(self, position):
        segment = Turtle()
        segment.penup()
        segment.shape('square')
        segment.shapesize(self.segment_size)
        segment.hideturtle()
        segment.setpos(position)
        self.snake_segments.append(segment)
        segment.showturtle()

    def grow(self, amount):
        spawn_pos = self.snake_segments[-1].pos()
        self.add_segment(spawn_pos)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(-90)

    def up(self):
        if self.head.heading() != -90:
            self.head.setheading(90)
