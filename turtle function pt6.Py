import turtle
screen = turtle.Screen()
screen.bgcolor("green")
screen.setup(600, 400)
screen.title("Hypnotising")
pen = turtle.Turtle()
size = 0
while True:
    for i in range(4):
        pen.fd(size + 1)
        pen.left(90)
        size = size - 5
    size += 1