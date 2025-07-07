num = int(input("Enter a number:"))
i = 0
while num > 0:
    num = num // 10
    i = i + 1
print("Number of digits:", i)