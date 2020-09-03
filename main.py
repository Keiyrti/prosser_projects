# Setting a 'class' and making a Menu Bar

from tkinter import *

window = Tk()
window.title("Menu Tutorial")


#Setting/Defining a 'class'
menu = Menu(window)

#Definining our top menu items
file = Menu(menu)
edit = Menu(menu)
exit = Menu(menu)

#Adding drop downs for each menu item
file.add_command(label='Open')
file.add_command(label='Edit')
file.add_command(label='Undo')
menu.add_cascade(label='File', menu=file)

#Adding drop downs for each menu item
edit.add_command(label='Copy')
edit.add_command(label='Cut')
edit.add_command(label='Paste')
menu.add_cascade(label='Edit', menu=edit)

exit.add_command(label='Exit')
menu.add_cascade(label='Exit', menu=exit, command=exit)


window.config(menu=menu)
window.mainloop()
