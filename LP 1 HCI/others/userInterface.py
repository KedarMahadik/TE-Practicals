import tkinter as tk
from tkinter import*
from tkinter import messagebox

root = tk.Tk()
root.title("Login")

def fun():
    messagebox.showinfo("Success","Successfully Done")
b1 = tk.Button(root, text = 'OK', command = fun)

check_var = IntVar()
check_var1 = IntVar()
check1 = tk.Checkbutton(root, text = 'Male',Variable = check_var, onvalue = 1, offvalue = 0 )
check1.pack()
check2 = tk.Checkbutton(root, text = 'Female',Variable = check_var1, onvalue = 1, offvalue = 0 )
check2.pack()

radio_var = IntVar()
radio1 = tk.Radiobutton(root, text =  " ", variable = radio_var, value = 1, command=fun )
radio1.pack()


root.mainloop()
