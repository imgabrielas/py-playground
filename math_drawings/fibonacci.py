import turtle
import math

# -----------------------------
# Screen setup
# -----------------------------
wn = turtle.Screen()
wn.setup(width=1200, height=800)
wn.title("Fibonacci Spiral")

# Enable RGB colors (0-255)
turtle.colormode(255)

# Turtle setup
myTurtle = turtle.Turtle()
myTurtle.speed(0)
myTurtle.pensize(3)
myTurtle.pencolor((55, 134, 237))  
myTurtle.hideturtle()


def main():
    """Calculate Fibonacci numbers and draw the squares."""
    valueOne = 0
    valueTwo = 1
    fib = 1

    for _ in range(8):            # Number of Fibonacci squares
        myTurtle.right(90)
        drawSq(fib * 20)

        fib = valueOne + valueTwo
        valueOne = valueTwo
        valueTwo = fib


def drawSq(side):
    """Draw one Fibonacci square."""
    for _ in range(6):
        myTurtle.forward(side)
        myTurtle.left(90)


def spiral():
    """Draw the Fibonacci spiral."""
    angle = 90

    myTurtle.right(90)
    myTurtle.penup()
    myTurtle.setpos(0, 0)
    myTurtle.pendown()

    radii = [20, 20, 40, 60, 100, 160, 260, 420]

    for r in radii:
        arc(r, angle)


def arcLine(n, length, angle):
    """Draw n short line segments."""
    for _ in range(n):
        myTurtle.forward(length)
        myTurtle.left(angle)


def arc(r, angle):
    """Draw an arc of radius r over the specified angle."""
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = angle / n

    myTurtle.left(step_angle / 2)
    arcLine(n, step_length, step_angle)
    myTurtle.right(step_angle / 2)


# -----------------------------
# Run program
# -----------------------------
main()
spiral()

wn.exitonclick()