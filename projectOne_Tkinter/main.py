                                                        #       IMPORTS        #
# Import all needed "parts"
from tkinter import *
import tkinter.ttk as ttk

from random import randint





                                                        #       VARIABLES      #
# Variables to track enemy health values
enemyHealth: int = round(randint(25, 50) * 1/10)
enemyHealthCurrent: int = enemyHealth

# Variable to track gold value
gold: int = 0

# Variables to track damage variables
strength: int = 1
allies: int = 0
killCount: int = 0

# Variables to track shop costs
strengthCost: int = 20
alliesCost: int = 50

firstNames: list = ["Helga", "Bulgrif", "Fluffy", "Chad", "Karen"]
lastNames: list = ["Crusher", "Mallet", "Sjorborn", "Pancakes", "Smith"]

playerName = f"{firstNames[randint(0, len(firstNames) - 1)]} {lastNames[randint(0, len(lastNames) - 1)]}"
print(playerName)

print(len(firstNames))


                                                        #     ROOT CREATION    #
# Create Tkinter window
window = Tk()
window.title("Clicker RPG")

# Change Theme
appTheme = ttk.Style()
appTheme.theme_use('winnative')
appTheme.configure("red.Horizontal.TProgressbar", foreground='red', background='red')





                                                        #       FUNCTIONS      #
# Function to close window
def close():
    window.destroy()


# Function to print values to the console
def print_console(text):
    consoleGUI.insert(END, f"{text}\n")
    consoleGUI.see("end")


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

        print_console("Strength upgraded.")

    else:
        print_console("Insufficient Gold.")

# Function to hire allies
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

        print_console("Ally hired.")

    else:
        print_console("Insufficient Gold.")


# Function to kill enemy
def kill():
    global enemyHealth
    global enemyHealthCurrent
    global playerName
    global gold
    global killCount

    randomMultiplier = randint(1, 3)
    goldGain = round((enemyHealth / 5) * randomMultiplier)
    gold += goldGain
    killCount += 1

    print_console(f"{enemyName['text']} Killed\nReceived {goldGain} Gold!\n")

    enemyHealth = round(randint(25, 50) * killCount/10)
    enemyHealthCurrent = enemyHealth

    enemyName["text"] = f"{firstNames[randint(0, len(firstNames) - 1)]} {lastNames[randint(0, len(lastNames) - 1)]}"

    if enemyName["text"] == playerName:
        print_console("You found yourself!\n")

    healthBar.config(maximum=enemyHealth, value=enemyHealth)
    goldLabel["text"] = f"Gold: {gold}"

    statsKillCount["text"] = f"Kills: {killCount}"


# Function to deal "ally damage" every second
def allies_attack():
    global enemyHealth
    global enemyHealthCurrent
    global strength

    enemyHealthCurrent -= allies * strength
    healthBar["value"] = enemyHealthCurrent

    # If enemy dies
    if healthBar["value"] <= 0:
        kill()

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
        kill()

    healthNumber.config(text=f"{enemyHealthCurrent}/{enemyHealth}")





                                                        #    PANEL CREATION    #
# Config column and row size + sizing
window.columnconfigure([0, 1, 2], weight=1, minsize=285)
window.rowconfigure(0, weight=1, minsize=570)


    #   #   #

# Add "Panels"
leftPanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
leftPanel.grid(sticky="ns")

middlePanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
middlePanel.grid(sticky="ns", column=1, row=0)

rightPanel = Frame(window, bg="#1e1e1e", padx=5, pady=10)
rightPanel.grid(sticky="ns", column=2, row=0)





                                                        #   LEFT PANEL ASSETS  #
# Display player statistics
statsTitle = Label(leftPanel, text="Statistics", bg="#1e1e1e", fg="#f1f1f1", font=("System", 20))
statsTitle.grid(pady=(50, 20))

statsName = Label(leftPanel, text=playerName, bg="#1e1e1e", fg="#f1f1f1", font=("System"))
statsName.grid(row=1, pady=(0, 30))

statsStrength = Label(leftPanel, text=f"Strength: {strength}", bg="#1e1e1e", fg="#f1f1f1", height=2, width=20, font=("System", 12))
statsStrength.grid(row=2)

statsAllies = Label(leftPanel, text=f"Allies: {allies}", bg="#1e1e1e", fg="#f1f1f1", height=2, width=20, font=("System", 12))
statsAllies.grid(row=3)

statsKillCount = Label(leftPanel, text=f"Kills: {killCount}", bg="#1e1e1e", fg="#f1f1f1", height=2, width=20, font=("System", 12))
statsKillCount.grid(row=4)


console = Frame(leftPanel, pady=30, bg="#1e1e1e")
console.grid(row=10, column=0)

consoleGUI = Text(console, bg="#0e0e0e", fg="#f1f1f1", height=15, width=30, font=("System"))
consoleGUI.grid(row=0,sticky="s")

consoleScrollbar = Scrollbar(console)
consoleScrollbar.grid(row=0, column=1, sticky='ns')

consoleGUI.config(yscrollcommand=consoleScrollbar.set)
consoleScrollbar.config(command=consoleGUI.yview)




                                                        #  MIDDLE PANEL ASSETS #
# Create new frame for health values
healthFrame = Frame(middlePanel, bg="#1e1e1e")
healthFrame.grid()

# Display enemy health bar
healthBar = ttk.Progressbar(healthFrame, mode='determinate', style="red.Horizontal.TProgressbar", maximum=enemyHealth,
                            value=enemyHealth, length=200)
healthBar.grid(row=0)

# Display enemy health number
healthNumber = Label(healthFrame, text=f"{enemyHealthCurrent}/{enemyHealth}", bg="#1e1e1e", fg="#f1f1f1", width=5, padx=10,
                     pady=50, font=("System", 20))
healthNumber.grid(row=0, column=1)


# Display enemy
enemy = Button(middlePanel, height=15, width=20, pady=10, command=attack)
enemy.grid(row=1)

enemyName = Label(middlePanel, text=f"{firstNames[randint(0, len(firstNames) - 1)]} {lastNames[randint(0, len(lastNames) - 1)]}", bg="#1e1e1e", fg="#f1f1f1", font=("System"))
enemyName.grid(row=2, pady=(0, 30))



                                                        #  RIGHT PANEL ASSETS  #
# Display gold value label
goldLabel = Label(rightPanel, text=f"Gold: {gold}", bg="#1e1e1e", fg="#f1f1f1", pady=50, font=("System", 20))
goldLabel.grid(row=1)


# Strength upgrade button
upgradeStrength = Button(rightPanel, text="Upgrade your strength!", bg="#0e0e0e", fg="#f1f1f1", height=2, width=20, command=buy_strength, font=("System", 12))
upgradeStrength.grid(row=2)

upgradeStrengthCost = Label(rightPanel, text=f"{strengthCost}", bg="#1e1e1e", fg="#f1f1f1", padx=10, font=("System", 12))
upgradeStrengthCost.grid(row=2, column=1)


# Allies upgrade button
upgradeAllies = Button(rightPanel, text="Hire new allies!", bg="#0e0e0e", fg="#f1f1f1", height=2, width=20, command=buy_allies, font=("System", 12))
upgradeAllies.grid(row=3)

upgradeAlliesCost = Label(rightPanel, text=f"{alliesCost}", bg="#1e1e1e", fg="#f1f1f1", padx=10, font=("System", 12))
upgradeAlliesCost.grid(row=3, column=1)





                                                        #     INITIATE ROOT    #
# Change window size and color
window.geometry("900x600")
window.config(bg='#1e1e1e')

# Initiate window
window.after(1000, allies_attack)
window.mainloop()
