import turtle

def drawsquare():
    window = turtle.Screen()
    window.bgcolor("Red")

    draw = turtle.Turtle()
    draw.shape("turtle")
    draw.color("green","yellow")
    draw.speed(2)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)
    draw.forward(100)
    draw.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

    window.exitonclick()

drawsquare()
