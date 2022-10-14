import turtle as t
from random import choice

rgb_colors = [(198, 13, 32), (250, 237, 18), (39, 76, 189), (39, 217, 69), (229, 159, 46),
              (237, 226, 6), (28, 40, 156), (215, 75, 13), (16, 154, 15), (198, 15, 11),
              (242, 35, 166), (229, 17, 121), (70, 10, 31), (62, 15, 8), (224, 140, 208), (11, 97, 62)]
tim = t.Turtle()
t.colormode(255)
tim.speed(10)
tim.hideturtle()
tim.penup()
start_x = -250
start_y = -250
tim.goto(start_x, start_y)
for i in range(10):
    tim.penup()
    tim.goto(start_x, start_y + 50 * i)
    for _ in range(10):
        tim.penup()
        tim.forward(50)
        rand_color = choice(rgb_colors)
        tim.pendown()
        tim.dot(20, rand_color)

screen = t.Screen()
screen.exitonclick()