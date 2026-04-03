
import tkinter as tk

def calculate():
    result.set(eval(entry.get()))

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=20)
entry.pack()

button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

result = tk.StringVar()
output = tk.Label(window, textvariable=result)
output.pack()

window.mainloop()
