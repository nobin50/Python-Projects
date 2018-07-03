import turtle

def triangle(draw):
    for i in range(3):
        draw.backward(150)
        draw.left(120)

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)

    for j in range(36):
        triangle(brad)
        brad.right(10)

    window.exitonclick()

drawing()
