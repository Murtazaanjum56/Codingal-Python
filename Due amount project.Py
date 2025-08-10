amount = int(input("How much was the product?"))
due = int(input("How much was paid?"))
need = 0
if due > amount:
    need = due - amount
    print("He owes you", need)
elif amount > due:
    neeed = amount - due
    print("You owe him", need)
elif amount == due:
    print("No one owes anything")
