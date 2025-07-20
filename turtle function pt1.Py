import turtle

turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()

num_sides = 6
legnth = 70
angle = 360 / num_sides

for i in range(num_sides):
  polygon.forward(legnth)
  polygon.right(angle)

turtle.done()