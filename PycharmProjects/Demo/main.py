import turtle

import colorgram
import turtle as t
import random

colors = colorgram.extract('Hirst.png', 20)
extracted_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    extracted_colors.append((r, g, b))


t.colormode(255)
todd = t.Turtle()
print(todd.pos())
todd.ht()
todd.penup()
todd.setpos(-550,-480)
todd.speed(0)

y_index = todd.ycor()
rows = 13
for _ in range(rows):
    for _ in range(13):
        todd.dot(50, random.choice(extracted_colors))
        todd.forward(85)
    y_index += 80
    todd.sety(y_index)
    todd.setheading(todd.heading() - 180)


print(turtle.window_height())
print(turtle.window_width())

screen = t.Screen()
screen.exitonclick()

