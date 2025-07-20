import turtle
turtle.Screen().bgcolor("brown")
turtle.Screen().setup(300,400)

shape = turtle.Turtle()
shape.color("white")

for i in range(4):
    shape.forward(100)
    shape.right(90)
turtle.done()