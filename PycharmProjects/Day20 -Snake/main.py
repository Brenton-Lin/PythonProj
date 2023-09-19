# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from turtle import Screen
import Snake
import time
import Fud
import ScoreBoard

SCREEN_SIZE = 600
X_BOUND = SCREEN_SIZE/2
Y_BOUND = SCREEN_SIZE/2


screen = Screen()
screen.setup(SCREEN_SIZE, SCREEN_SIZE)
screen.bgcolor("green")
screen.title("Snek")
screen.tracer(0)

# generate snake
snake = Snake.Snake(3)
food = Fud.Fud()
print(food.class_attribute)

# Score setup
score_board = ScoreBoard.ScoreBoard()
screen.update()

# register input events
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


'''basic movement prototype'''
run = True
while run:
    # head should always move
    screen.update()
    time.sleep(0.10)
    snake.move()
    # every other segment just needs to follow the next in line

    # detect food collision
    if snake.head.distance(food) < 15:
        snake.grow(1)
        food.refresh()
        score_board.increase(1)

    # detect wall collision
    if snake.head.xcor() > X_BOUND or snake.head.xcor() < -X_BOUND:
        run = False
    if snake.head.ycor() > Y_BOUND or snake.head.ycor() < -Y_BOUND:
        run = False

    # Detect tail collision
    # We can rewrite this with slices and tuples
    # Look how I can slice segments for the loop, rather than defining a range, now the iterator references
    # a segment rather than an index for the snake_segment array.
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            run = False

score_board.game_over()

screen.exitonclick()
