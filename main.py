# Setting a 'class' and making a Menu Bar

from tkinter import *

window = Tk()
window.title("Clicker RPG")


# Setting/Defining a 'class'
menu = Menu(window)

# Definining our top menu items
file = Menu(menu)
edit = Menu(menu)
exit = Menu(menu)

# Add first button
window.columnconfigure([0, 1, 2], weight=1, minsize=300)
window.rowconfigure(0, weight=1, minsize=600)

leftPanel = Frame(window)
middlePanel = Frame(window)
rightPanel = Frame(window)

leftPanel.grid()
middlePanel.grid(column=1, row=0)
rightPanel.grid(column=2, row=0)

leftLabel = Label(leftPanel, text="TestLeft")
leftLabel.grid()

middleLabel = Label(middlePanel, text="TestMiddle")
middleLabel.grid()

rightLabel = Label(rightPanel, text="TestRight")
rightLabel.grid()

# Adding drop downs for each menu item
file.add_command(label='Open')
file.add_command(label='Edit')
file.add_command(label='Undo')
menu.add_cascade(label='File', menu=file)

# Adding drop downs for each menu item
edit.add_command(label='Copy')
edit.add_command(label='Cut')
edit.add_command(label='Paste')
menu.add_cascade(label='Edit', menu=edit)

exit.add_command(label='Exit')
menu.add_cascade(label='Exit', menu=exit, command=exit)

window.geometry("900x600")
window.config(menu=menu, bg='#1e1e1e')
window.mainloop()


# wacky edit


# random edit


# another edit
