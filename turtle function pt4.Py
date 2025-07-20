import turtle
turtle.Screen().bgcolor("black")
turtle.Screen().setup(300,400)
shape = turtle.Turtle()
shape.color("yellow")
for i in range(2):
    shape.forward(100)
    shape.right(90)
    shape.forward(50)
    shape.right(90)
turtle.done()