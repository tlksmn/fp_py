from tkinter import *
from tkinter import ttk
from rx.subject import Subject

root = Tk()
root.title("Validation_form")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=2, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

root.mainloop()

