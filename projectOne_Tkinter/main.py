                                                        #       IMPORTS        #
# Import all needed "parts"
from tkinter import *
import tkinter.ttk as ttk

from random import randint





                                                        #       VARIABLES      #
# Variables to track enemy health values
enemyHealth: int = randint(25, 50)
enemyHealthCurrent: int = enemyHealth

# Variable to track gold value
gold: int = 0

# Variables to track damage variables
strength: int = 1
allies: int = 0

# Variables to track shop costs
strengthCost: int = 20
alliesCost: int = 50





                                                        #     ROOT CREATION    #
# Create Tkinter window
window = Tk()
window.title("Clicker RPG")

# Change Theme
s = ttk.Style()
s.theme_use('winnative')
s.configure("red.Horizontal.TProgressbar", foreground='red', background='red')





                                                        #       FUNCTIONS      #
# Function to close window
def close():
    window.destroy()


# Function to upgrade strength
def buy_strength():
    global gold
    global strength
    global strengthCost
    if gold >= strengthCost:
        gold -= strengthCost
        strengthCost = round(strengthCost * 1.5)
        strength += 1
        goldLabel["text"] = f"Gold: {gold}"
        upgradeStrengthCost["text"] = f"{strengthCost}"
        statsStrength["text"] = f"Strength: {strength}"

def buy_allies():
    global gold
    global allies
    global alliesCost
    if gold >= alliesCost:
        gold -= alliesCost
        alliesCost = round(alliesCost * 2)
        allies += 1
        goldLabel["text"] = f"Gold: {gold}"
        upgradeAlliesCost["text"] = f"{alliesCost}"
        statsAllies["text"] = f"Allies: {allies}"


# Function to kill enemy
def death():
    global enemyHealth
    global enemyHealthCurrent
    global gold

    randomMultiplier = randint(1, 3)
    gold += round((enemyHealth / 5) * randomMultiplier)

    enemyHealth = randint(25, 50)
    enemyHealthCurrent = enemyHealth

    healthBar.config(maximum=enemyHealth, value=enemyHealth)
    goldLabel.config(text=f"Gold: {gold}")


# Function to deal "ally damage" every second
def allies_attack():
    global enemyHealth
    global enemyHealthCurrent
    global strength

    enemyHealthCurrent -= allies * strength
    healthBar["value"] = enemyHealthCurrent

    # If enemy dies
    if healthBar["value"] <= 0:
        death()

    healthNumber.config(text=f"{enemyHealthCurrent}/{enemyHealth}")
    window.after(1000, allies_attack)


# Function to deal damage per click
def attack():
    global enemyHealth
    global enemyHealthCurrent

    enemyHealthCurrent -= strength
    healthBar["value"] = enemyHealthCurrent

    # If enemy dies
    if healthBar["value"] <= 0:
        death()

    healthNumber.config(text=f"{enemyHealthCurrent}/{enemyHealth}")





                                                        #    PANEL CREATION    #
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





                                                        #   LEFT PANEL ASSETS  #
# Test Label
leftLabel = Label(leftPanel, text="Left Panel", bg="#1e1e1e", fg="#f1f1f1")
leftLabel.grid()

statsTitle = Label(leftPanel, text="Statistics", bg="#1e1e1e", fg="#f1f1f1", pady=50)
statsTitle.grid(row=1)

statsStrength = Label(leftPanel, text=f"Strength: {strength}", bg="#1e1e1e", fg="#f1f1f1")
statsStrength.grid(row=2)

statsAllies = Label(leftPanel, text=f"Allies: {allies}", bg="#1e1e1e", fg="#f1f1f1")
statsAllies.grid(row=3)





                                                        #  MIDDLE PANEL ASSETS #
# Test Label
middleLabel = Label(middlePanel, text="Middle Panel", bg="#1e1e1e", fg="#f1f1f1")
middleLabel.grid()

# Display enemy health bar
healthBar = ttk.Progressbar(middlePanel, mode='determinate', style="red.Horizontal.TProgressbar", maximum=enemyHealth,
                            value=enemyHealth, length=200)
healthBar.grid(row=1)

# Display enemy health number
healthNumber = Label(middlePanel, text=f"{enemyHealthCurrent}/{enemyHealth}", bg="#1e1e1e", fg="#f1f1f1", padx=10,
                     pady=50)
healthNumber.grid(row=1, column=1)

# Display enemy
enemy = Button(middlePanel, height=15, width=20, pady=10, command=attack)
enemy.grid(row=2)





                                                        #  RIGHT PANEL ASSETS  #
# Test Label
rightLabel = Label(rightPanel, text="RightPanel", bg="#1e1e1e", fg="#f1f1f1")
rightLabel.grid()

# Display gold value label
goldLabel = Label(rightPanel, text=f"Gold: {gold}", bg="#1e1e1e", fg="#f1f1f1", pady=50)
goldLabel.grid(row=1)

# Strength upgrade button
upgradeStrength = Button(rightPanel, text="Upgrade your strength!", height=2, width=20, command=buy_strength)
upgradeStrength.grid(row=2)

upgradeStrengthCost = Label(rightPanel, text=f"{strengthCost}", bg="#1e1e1e", fg="#f1f1f1", padx=10)
upgradeStrengthCost.grid(row=2, column=1)

# Allies upgrade button
upgradeAllies = Button(rightPanel, text="Hire new allies!", height=2, width=20, command=buy_allies)
upgradeAllies.grid(row=3)

upgradeAlliesCost = Label(rightPanel, text=f"{alliesCost}", bg="#1e1e1e", fg="#f1f1f1", padx=10)
upgradeAlliesCost.grid(row=3, column=1)





                                                        #     INITIATE ROOT    #
# Change window size and color
window.geometry("900x600")
window.config(bg='#1e1e1e')

# Initiate window
window.after(1000, allies_attack)
window.mainloop()
