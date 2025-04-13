import turtle

def draw_heart():
    """Draws a heart shape."""
    t.begin_fill()
    t.fillcolor("red")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

def draw_star():
    """Draws a star."""
    t.penup()
    t.goto(-50, 50)  # Move to position inside the heart
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(100)
        t.right(144)
    t.end_fill()

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("pink")
t = turtle.Turtle()
t.speed(3)

# Draw the heart
draw_heart()

# Draw the star inside the heart
draw_star()

# Hide the turtle and display the drawing
t.hideturtle()
screen.mainloop()