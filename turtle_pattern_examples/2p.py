import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "yellow", "purple", "white"]

for i in range(1500):
    t.color(colors[i % len(colors)])
    t.forward(math.sqrt(i) * 10)
    t.right(89)

turtle.done()