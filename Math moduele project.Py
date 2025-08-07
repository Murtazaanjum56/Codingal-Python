import random
import math

choice = str(input("Choose an option (sin, cos, tan):").lower())
degrees = float(input("Great choice, Enter the angle in degrees: "))
radians = math.radians(degrees)
if choice == "sin":
    result = math.sin(radians)
elif choice == "cos":
    result = math.cos(radians)
elif choice == "tan":
    result = math.tan(radians)
print(f"Thw {choice} of {degrees} degrees is : {result}")