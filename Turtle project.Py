import turtle

shape = turtle.Turtle()
turtle.Screen().setup(300, 400)
turtle.Screen().bgcolor("orange")

square = 4

for i in range(square):
    shape.forward(70)
    shape.right(90)