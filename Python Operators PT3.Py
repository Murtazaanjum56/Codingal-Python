Amount = int(input("Enter an amount to withdraw:"))

note100 = Amount // 100
note50 =  (Amount%100)//50
note10 = ((Amount%100)%50)//10
print("Number of 100 notes:", note100)
print("Number of 50 notes:", note50)
print("Number of 10 notes:", note10)
