import turtle

# Setup screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("skyblue")

# Create turtle object
t = turtle.Turtle()
t.speed(0)

# Function to draw the sun
def draw_sun():
    t.penup()
    t.goto(250, 200)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

# Function to draw a cloud
def draw_cloud(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(3):
        t.circle(20)
        t.penup()
        t.goto(x + 30, y - 10)
        t.pendown()
        x += 30
    t.end_fill()

# Function to draw the grass
def draw_grass():
    t.penup()
    t.goto(-400, -100)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(800)
    t.right(90)
    t.forward(300)
    t.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(60)
    t.end_fill()

    # Draw leaves
    t.color("darkgreen")
    t.penup()
    t.goto(x - 15, y + 40)
    t.pendown()
    t.begin_fill()
    t.circle(30)
    t.end_fill()

# Function to draw a house
def draw_house():
    # Draw base
    t.penup()
    t.goto(-100, -100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(4):
        t.forward(200)
        t.left(90)
    t.end_fill()

    # Draw roof
    t.color("brown")
    t.begin_fill()
    t.goto(-100, 100)
    t.goto(0, 200)
    t.goto(100, 100)
    t.goto(-100, 100)
    t.end_fill()

# Function to draw flowers
def draw_flower(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("purple")
    for _ in range(6):
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.right(60)
        t.pendown()

# Draw environment
draw_sun()
draw_cloud(-200, 180)
draw_cloud(100, 220)
draw_grass()
draw_tree(-250, -50)
draw_tree(150, -80)
draw_house()
draw_flower(-50, -120)
draw_flower(80, -130)
draw_flower(200, -140)

# Finish
turtle.done()