from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("300x400")

def calc():
    p = float(p_entry.get())
    r = float(r_entry.get())
    t = float(t_entry.get())
    a = p * (1 + r/100)*t
    result_label.config(text=f"Amount: {a:.2f}")

Label(window, text="Principal").pack()
p_entry = Entry(window)
p_entry.pack()

Label(window, text="Rate").pack()
r_entry = Entry(window)
r_entry.pack()

Label(window, text="years").pack()
t_entry = Entry(window)
t_entry.pack()

Button(window, text="Calculate", command=calc).pack()

result_label = Label(window, text="")
result_label.pack()

window.mainloop()