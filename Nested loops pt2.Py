low = int(input("Enter the lower limit: "))
up = int(input("Enter the upper limit: "))

print("The prime numbers between", low, "and", up, "are:")
for num in range(low, up + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)