import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)

pen.color("green")

for _ in range(4):
    pen.forward(100)
    pen.right(90)

turtle.done()