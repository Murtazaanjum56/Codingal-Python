# Chech if student has medical cause for attendance
med_cause = str(input("Does your student have a medical cause for attendance?: Y/N"))

atten = int(input("How much percentage is your student's attendance?: "))

if med_cause == "Y":
    print("Your student is excused from attendance.")
else: 
    if atten >= 75:
        print("Your student is excused from attendance.")
    else:
        print("Your student is not excused from attendance.")