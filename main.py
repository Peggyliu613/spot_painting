from turtle import Turtle, Screen
# import colorgram
import random

# colorgram_colors = colorgram.extract('image.jpg', 20)

# colors = []
# for color in colorgram_colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     colors.append(new_color)

colors = [(236, 235, 230), (239, 228, 234), (223, 240, 231), (227, 232, 241), (240, 37, 113), (146, 25, 72), (218, 161, 64), (14, 144, 88), (239, 73, 35), (186, 169, 36), (29, 127, 193), (56, 190, 230), (245, 220, 53), (178, 42, 102), (35, 175, 119), (129, 189, 104), (78, 27, 81), (209, 62, 28), (251, 226, 0), (146, 31, 26)]

shu = Turtle()
screen = Screen()
screen.colormode(255)

shu.hideturtle()
shu.shape("turtle")
shu.penup()
shu.goto(-225, -225)

for _ in range(10):
    shu.dot(20, random.choice(colors))
    for _ in range(9):
        shu.fd(50)
        shu.dot(20, random.choice(colors))
    shu.goto(shu.position()[0]-450, shu.position()[1] + 50)


screen.exitonclick()
