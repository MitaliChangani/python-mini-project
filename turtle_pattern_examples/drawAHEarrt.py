import turtle

# Create turtle screen
screen = turtle.Screen()
screen.bgcolor("pink")

# Create turtle instance
t = turtle.Turtle()
t.speed(1)
t.color("red")

# Begin filling the heart with color
t.begin_fill()

# Move to starting position
t.left(140)
t.forward(180)

# Create the left curve
t.circle(-90, 200)
t.left(120)

# Create the right curve
t.circle(-90, 200)
t.forward(180)

# Fill the heart shape
t.end_fill()

# Hide the turtle and display the drawing
t.hideturtle()
screen.mainloop()