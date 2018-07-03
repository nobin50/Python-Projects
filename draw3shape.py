import turtle

brad = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("red")

def square():
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)

    for i in range(4):
        brad.forward(150)
        brad.right(90)

def triangle():
    brad.shape("arrow")
    brad.color("green")
    brad.speed(2)

    for i in range(3):
        brad.backward(150)
        brad.left(120)

def circle():
    brad.shape("circle")
    brad.color("blue")
    brad.speed(3)

    brad.circle(100)

square()
triangle()
circle()
window.exitonclick()
