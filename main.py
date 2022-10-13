from turtle import Turtle, Screen
from random import random



tim = Turtle()
tim.shape("turtle")
tim.color("red")
print(tim.screen.colormode())
#tim.pencolor(randint(255),randint(255),randint(255))
for i in range(3, 11):
    rgb_color = (random(), random(), random())
    tim.pencolor(rgb_color)
    angle = 360 / i

    for j in range(i):
        tim.forward(100)
        tim.right(angle)



    # tim.penup() if i % 2 else tim.pendown()
    # tim.forward(10)





screen = Screen()
screen.exitonclick()