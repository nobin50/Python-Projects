import turtle

def draw_square(draw):
    for i in range(4):
        draw.forward(100)
        draw.right(90)

def drawing():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    for j in range(36):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

drawing()
