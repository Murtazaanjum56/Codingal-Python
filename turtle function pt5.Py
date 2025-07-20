import turtle
turtle.Screen().bgcolor("lightblue")
turtle.Screen().setup(500, 400)

shape = turtle.Turtle()
shape.color("purple")

shape.forward(100) # draw a base

for i in range(2):
    shape.left(120)
    shape.forward(100) # draw the sides of the triangle

shape.penup()
shape.right(150)
shape.forward(50)

shape.pendown()
shape.right(90)
shape.forward(100)

for i in range(2):
    shape.right(120)
    shape.forward(100) # draw the other sides of the triangle

turtle.done()