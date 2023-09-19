from turtle import Screen
from Paddle import Paddle
import time
from Ball import Ball

# Pong Planning
# Classes:

# Paddles

# Ball

# Scoreboard


# Tasks

# Create Screen

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
X_BOUND = SCREEN_WIDTH / 2
Y_BOUND = SCREEN_HEIGHT / 2

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("DONG")
screen.tracer(0)

# Game setup
right_paddle = Paddle(360, 0)
left_paddle = Paddle(-360, 0)
ball = Ball()
screen.update()

screen.listen()
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

run_game = True
while run_game:
    ball.move()
    screen.update()
    time.sleep(0.08)

    # East/West collision detection
    if ball.xcor() > 380:
        ball.reset_pos()
    if ball.xcor() < -380:
        ball.reset_pos()
    # Top Collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    # Paddle Collisions
    if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.paddle_bounce()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -340:
        ball.paddle_bounce()

screen.exitonclick()
