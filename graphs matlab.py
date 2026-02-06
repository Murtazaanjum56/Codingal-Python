import matplotlib.pyplot as plt

students = ["john", "alissa", "adam", "aliza", "bob", "fatima", "david", "alina"]
marks = [85, 90, 78, 92, 88, 76, 95, 89]

percentage = []
for x in marks:
    res = (x/100) * 100
    percentage.append(res)

print(percentage)

def marks_line_chart(students, marks):
    plt.plot(students, marks)
    plt.title("Score of students")
    plt.xlabel("Student names")
    plt.ylabel("Marks")
    plt.show()

marks_line_chart(students, marks)

def precentage_bar_chart(students, percentage):
    plt.bar(students, percentage)
    plt.title("Students percentage graph")
    plt.xlabel("Student names")
    plt.ylabel("Percentage")
    plt.show()

precentage_bar_chart(students, percentage)