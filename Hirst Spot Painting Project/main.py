import turtle as t
import colorgram
import random

"""Draws a line of 10 dots of size 20 and space 50 and changes direction"""
def draw_line():
    for _ in range(9):
        john.dot(20, random.choice(rgb_colors))
        john.forward(50)
    john.dot(20, random.choice(rgb_colors))
    john.setheading(90)
    john.forward(50)

"""Draws the 2 line pattern"""
def two_lines():
    draw_line()
    john.setheading(180)
    draw_line()
    john.setheading(0)

colors = colorgram.extract('image.jpg', 30)
rgb_colors =[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

t.colormode(255)
john = t.Turtle()
john.shape("turtle")
john.speed(9)
john.penup()
john.hideturtle()
john.goto(-300, -250)

"""Crates a 10x10 dot pattern"""
for _ in range(5):
    two_lines()

screen = t.Screen()
screen.exitonclick()

