import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's speed
t.speed(10)

# Set the turtle's font size
t.write("Happy Makar Sankranti", align="center", font=("Lucida Fax", 24, "bold"))

# Move the turtle to a new location
t.penup()
t.goto(250, 0)
t.pendown()

# Draw a few shapes and colors to make it look like kite
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()
t.goto(-250, -50)
t.pendown()
t.color("blue")
t.begin_fill()
t.circle(50)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.exitonclick()