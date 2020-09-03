# Setting a 'class' and making a Menu Bar

from tkinter import *
import tkinter.ttk as ttk
from random import randint


enemyHealth = randint(25,50)


window = Tk()
window.title("Clicker RPG")

# Change Theme
s = ttk.Style()
s.theme_use('winnative')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')


# Setting/Defining a 'class'
menu = Menu(window)

# Definining our top menu items
file = Menu(menu)
edit = Menu(menu)
exit = Menu(menu)

# Config column and row size + sizing
window.columnconfigure([0, 1, 2], weight=1, minsize=285)
window.rowconfigure(0, weight=1, minsize=570)



# Add "Panels"
leftPanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
leftPanel.grid(sticky="ns")

middlePanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
middlePanel.grid(sticky="ns", column=1, row=0)

rightPanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
rightPanel.grid(sticky="ns", column=2, row=0)



# LEFT PANEL ASSETS
leftLabel = Label(leftPanel, text="Left Panel", bg="#1e1e1e", fg="#f1f1f1")
leftLabel.grid()


# MIDDLE PANEL ASSETS
middleLabel = Label(middlePanel, text="Middle Panel", bg="#1e1e1e", fg="#f1f1f1")
middleLabel.grid()

healthBar = ttk.Progressbar(middlePanel, mode='determinate', style="red.Horizontal.TProgressbar", maximum=enemyHealth, value=enemyHealth, length=250)
healthBar.grid(row=1)


def attack():
    global enemyHealth
    healthBar["value"] -= 1

    if healthBar["value"] <= 0:
        enemyHealth = randint(25,50)
        healthBar.config(maximum=enemyHealth, value=enemyHealth)

enemy = Button(middlePanel, height=15, width=20, pady=10, command=attack)
enemy.grid(row=2)


# RIGHT PANEL ASSETS
rightLabel = Label(rightPanel, text="RightPanel", bg="#1e1e1e", fg="#f1f1f1")
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
