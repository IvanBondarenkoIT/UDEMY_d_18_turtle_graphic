import turtle as t
from random import random, choice, randint


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def step_forward(distance):
    tim.pencolor(random_color())
    tim.forward(distance)

def draw_x_angle():
    for i in range(3, 11):
        tim.pencolor(random_color())
        angle = 360 / i
        for j in range(i):
            tim.forward(100)
            tim.right(angle)


def draw_random_move(repits: int=100):
    for _ in range(repits):
        angle = choice(directions)
        tim.setheading(angle)
        step_forward(20)


def draw_spirograph(radius: int=80):

    tim.pensize(1)
    angle = 0
    while angle < 360:
        tim.pencolor(random_color())
        tim.circle(radius)
        tim.right(5)
        angle += 5


tim = t.Turtle()
t.colormode(255)

directions = [0, 90, 180, 270]
tim.shape("turtle")
tim.color("red")
tim.pensize(5)
tim.speed(10)

draw_x_angle()
draw_random_move()
draw_spirograph()




screen = t.Screen()
screen.exitonclick()