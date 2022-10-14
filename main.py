import turtle as t
from random import random, choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def step_forward(tim, distance):
    tim.pencolor(random_color())
    tim.forward(distance)

def x_angle_drow():
    for i in range(3, 11):
        tim.pencolor(random_color())
        angle = 360 / i
        for j in range(i):
            tim.forward(100)
            tim.right(angle)


def random_move():
    for _ in range(100):
        angle = choice(directions)
        tim.setheading(angle)
        step_forward(tim, 20)


tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]
tim.shape("turtle")
tim.color("red")
tim.pensize(5)
tim.speed(10)

x_angle_drow()
random_move()


screen = t.Screen()
screen.exitonclick()