from turtle import Turtle, Screen
import random

shu = Turtle()
screen = Screen()
shu.shape("turtle")
shu.color("grey")
shu.turtlesize(3, 3)


def draw_dashed_line():
    for _ in range(10):
        shu.forward(10)
        shu.penup()
        shu.forward(10)
        shu.pendown()


def draw_polygon():
    i = 3
    colors = ["red", "orange", "wheat", "green", "blue", "blue3", "BlueViolet", "brown"]
    while i <= 10:
        shu.pencolor(colors[i - 3])
        for _ in range(i):
            shu.forward(50)
            shu.right(360/i)
        i += 1


def draw_random_walk():
    screen.colormode(255)
    directions = [0, 90, 180, 270]
    shu.pensize(10)
    while True:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        shu.pencolor((red, green, blue))
        shu.right(random.choice(directions))
        shu.forward(50)


def draw_spirograph():
    screen.colormode(255)
    i = shu.heading()
    shu.speed("fastest")
    while i <= 360:
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        shu.pencolor((red, green, blue))
        shu.circle(120)
        shu.setheading(i)
        shu.circle(120)
        i += 10


screen.exitonclick()
