from tkinter import *

root  = Tk()
root.geometry("500x500")
root.title("Menu Adding")
menubar = Menu(root)


file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = file)
file.add_command(label='New File', command = None)
file.add_command(label='Open...', command = None)
file.add_command(label='Save', command = None)
file.add_separator()
file.add_command(label='Exit', command = root.destroy)
root.config(menu = menubar)

edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label='Edit', menu = edit)
edit.add_command(label='Undo', command = None)
edit.add_command(label='Redo', command = None)
edit.add_separator()
edit.add_command(label='Cut', command = None)
edit.add_command(label='Copy', command = None)
edit.add_command(label='Paste', command = None)
edit.add_command(label='Find...', command = None)
edit.add_command(label='Find&Replace...', command = None)
edit.add_command(label='FindPage', command = edit)

insert = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Insert', menu = insert)
insert.add_command(label = 'Image', command = None)
insert.add_command(label = 'Video', command = None)
insert.add_command(label = 'Shape', command = None)
insert.add_command(label = 'Object', command = None)

root.mainloop()