import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")
clock = tk.Label(root, font=("Arial", 48, "bold"), bg="black", fg="white", padx=20, pady=10)
clock.pack()

def update_clock():
    clock.config(text=strftime("%I:%M:%S %p"))
    clock.after(1000, update_clock)

update_clock()
root.mainloop()