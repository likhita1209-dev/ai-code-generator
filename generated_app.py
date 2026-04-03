
from tkinter import *

root = Tk()
root.title("Login App")

label_1 = Label(root, text="Username")
label_1.pack()
entry_1 = Entry(root)
entry_1.pack()

label_2 = Label(root, text="Password")
label_2.pack()
entry_2 = Entry(root, show="*")
entry_2.pack()

button = Button(root, text="Login")
button.pack()

root.mainloop()
