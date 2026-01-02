from tkinter import *

# Create main window

window = Tk()

window.title("Frames")

window.geometry("400x300")

nums = [

[9, 8, 7],

[6, 5, 4],

[3, 2, 1],

['#', 0, '*']

]

# Build grid (4 rows × 3 columns)

for i in range(4): # 4 rows

  window.rowconfigure(i, weight=1, minsize=75)

  for j in range(3): # 3 columns

    window.columnconfigure(j, weight=1, minsize=50)
    frame = Frame(

    master=window,
    relief=SUNKEN,
    borderwidth=1
    )
    frame.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
    label = Label(
    master=frame,
    text=nums[i][j],
    font=("Arial", 16)

)
    label.pack(expand=True)
window.mainloop()