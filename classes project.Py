class Homework():
    def __init__(self, radius):
        self.radius = radius  # ✅ Use the parameter passed in

    def area(self):
        area1 = 3.14 * (float(self.radius) ** 2)
        print("The area of the circle is:", area1)

    def cir(self):
        cir1 = 2 * 3.14 * float(self.radius)
        print("The circumference of the circle is:", cir1)

rad = input("Enter the radius of the circle: ")
lets_see = Homework(rad)
lets_see.area()
lets_see.cir()
