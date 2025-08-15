import math
def Circle(diameter):
  """  This is a function to help you calculate the circumfrence of a circle."""
  diameter = float(input("Enter the diameter of the circle:"))
  print(f"The circumfrence of the circle is: {math.pi * diameter}")

Circle(0)