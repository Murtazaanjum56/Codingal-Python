range1 = int(input("Enter how many values you want to add to the list: "))
oddlist = []
evenlist = []

for i in range(range1):
    value = int(input("Enter a value: "))
    value = value * value
    if value % 2 == 0:
        evenlist.append(value)
    else:
        oddlist.append(value)


print("List of squares of odd numbers:", oddlist)
print("List of squares of even numbers:", evenlist)
