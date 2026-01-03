from tkinter import *
from tkinter import messagebox

window = Tk()

window.geometry("300x400")
window.title("Message Box Example")

def msg():
    messagebox.showwarning("Alert!", "Stop virus has been detected")

button = Button(window, text = "Scan for virus", command=msg)

button.place(x= 60, y = 30)
window.mainloop()