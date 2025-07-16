num = int(input("Enter a  number: "))
squ = 0
att = 0
                
for i in range(1, num + 1):
    squ += 1
    att = squ * squ
    if att == num:
        print("The square root of", num, "is", squ)
        break
    