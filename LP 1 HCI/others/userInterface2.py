import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login")
root.geometry("500x500")
root.configure(bg = '')

# Function to display the status of selections
def fun():
    male_selected = check_var.get()
    female_selected = check_var1.get()
    radio_selection = radio_var.get()

    message = "Successfully Done\n"

    # Check the Checkbuttons
    if male_selected and female_selected:
        message += "Both Male and Female selected."
    elif male_selected:
        message += "Male selected."
    elif female_selected:
        message += "Female selected."
    else:
        message += "No gender selected."

    # Check the Radiobutton
    if radio_selection == 1:
        message += " Radio button option selected."

    messagebox.showinfo("Status", message)

# Create Checkbuttons
L = tk.Label(root,text = "Student Registration form ",font= 20)
L.pack()

L1 = tk.Label(root,text = "Students Name: ",font= 20)
L1.place(x = '100',y = '100')
e1 = tk.Entry(root, font=20)
e1.place(x= '240',y = '100')

L2 = tk.Label(root, text = "Fathers name: ", font= 20)
L2.place(x = '100', y = '150')
e2 = tk.Entry(root,font=20)
e2.place(x= '240',y = '150')

L3 = tk.Label(root, text = "Gender:  ", font= 20)
L3.place(x = '100', y = '200')



check_var = tk.IntVar()
check_var1 = tk.IntVar()
check1 = tk.Checkbutton(root, text='Male', variable=check_var, onvalue=1, offvalue=0)
check1.place(x= '200', y = '200')
check2 = tk.Checkbutton(root, text='Female', variable=check_var1, onvalue=1, offvalue=0)
check2.place(x= '270', y = '200')

L4 = tk.Label(root, text = "Language Known :  ", font= 20)
L4.place(x = '100', y = '250')

# Create Radiobutton
radio_var = tk.IntVar()
radio_var1 = tk.IntVar()
radio_var2 = tk.IntVar()

radio1 = tk.Radiobutton(root, text="Marathi", variable=radio_var, value=1, font= 20)
radio1.place(x = '250', y = '250')
radio2 = tk.Radiobutton(root, text="Hindi", variable=radio_var1, value=1, font= 20)
radio2.place(x = '340', y = '250')
radio3 = tk.Radiobutton(root, text="English", variable=radio_var2, value=1, font= 20)
radio3.place(x = '420', y = '250')

L5 = tk.Label(root,text = "Email ID:  ",font= 20)
L5.place(x = '100',y = '300')
e3 = tk.Entry(root, font=20)
e3.place(x= '240',y = '300')

L6 = tk.Label(root,text = "Contact No: ",font= 20)
L6.place(x = '100',y = '350')
e4 = tk.Entry(root, font=20)
e4.place(x= '240',y = '350')


L7 = tk.Label(root,text = "Address:  ",font= 20)
L7.place(x = '100',y = '400')
e5 = tk.Entry(root, font=20)
e5.place(x= '240',y = '400')

# Create OK Button
b1 = tk.Button(root, text='SUBMIT', command=fun)
b1.place(x = '300', y = '450')

root.mainloop()
