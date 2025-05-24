import turtle
import random

# Setup Turtle
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
colors = ["red", "blue", "green", "yellow", "purple", "orange", "white"]

def draw_hexagon(x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(random.choice(colors))

    for _ in range(6):
        t.forward(size)
        t.right(60)

def draw_fractal(x, y, size, depth):
    if depth == 0:
        return
    draw_hexagon(x, y, size)
    
    offsets = [(-size, -size//2), (size, -size//2), (0, -size),
               (-size, size//2), (size, size//2), (0, size)]
    
    for dx, dy in offsets:
        draw_fractal(x + dx, y + dy, size // 2, depth - 1)

# Start drawing
draw_fractal(0, 0, 100, 4)

turtle.done()