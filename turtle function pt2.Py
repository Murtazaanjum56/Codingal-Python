import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(300,400)

circle = turtle.Turtle()

for i in range(360):
    circle.forward(1)
    circle.right(1)
turtle.done()