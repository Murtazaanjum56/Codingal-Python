row = int(input("Enter amount of rows"))
num = 0
print("Floyd's Triangle")
for i in range(1, row + 1): # outer loop for number of rows
    for j in range(1, i + 1):  # inner loop for number of columns
        num += 1
        print(num, end = "  ")
    print()
   
   