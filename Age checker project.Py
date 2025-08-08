age = None
while True:
    try:
      age = int(input("Enter your age: "))
      if age > 0:
        break
        
    except ValueError:
        print("Invalid Input, PLease enter a valid age.")

if age % 2 == 0:
    print("Your age is an even number.")
else:
    print("Your age is an odd number.")

number = None

while True:
    try:
        number = int(input("Enter a number to Divide by 50: "))
        result = 50 / number
        if result == True:
            print(re)
            break
    except ZeroDivisionError:
        print("Cannot divide by zero, please enter a valid number.")
        

        