import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)

pen.color("pink")

for _ in range(3):
    pen.forward(100)
    pen.left(120)

turtle.done()