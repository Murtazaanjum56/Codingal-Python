print("Enter percentage of marks obtained in each subject")
math = int(input("Mths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

sum = math + english + science + hindi
print("Total marks obtained:", sum, "out of 400")

average = (sum/400) * 100
print("Average percentage of marks obtained:", average)
