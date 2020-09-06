"""
Idle Clicker Game by Jack, Dane, and Autum
Prosser Group Project #1
"""

    #       IMPORTS        #


# Import all needed "parts"
import tkinter
import tkinter.ttk as ttk

from random import randint


    #       CLASSES        #


class EnemyValues():
    """Class to track enemy values"""
    def __init__(self):
        self.reset()
    def reset(self):
        """Method used to reset the values of ENEMY"""
        self.randomize_name()
        self.randomize_health()
    def randomize_name(self):
        """Method used to randomize the name value"""
        self.name = (f"{firstNames[randint(0, len(firstNames) - 1)]}"
                      + f" {lastNames[randint(0, len(lastNames) - 1)]}")
    def randomize_health(self):
        """Method used to randomize the health value"""
        self.health = round(randint(25, 50) * 1 / 10)
        self.health_current = self.health
    name: str
    health: int
    health_current: int


class PlayerValues:
    """Class to track player values"""
    def __init__(self):
        self.name = (f"{firstNames[randint(0, len(firstNames) - 1)]}"
                      + f" {lastNames[randint(0, len(lastNames) - 1)]}")
    name: str
    strength: int = 1
    crit_chance: int = 5
    allies: int = 0
    gold: int = 0
    kill_count: int = 0


class ShopValues:
    """Class to track shop values"""
    strength_cost: int = 20
    allies_cost: int = 50


    #       VARIABLES      #


firstNames: list = ["Helga", "Bulgrif", "Fluffy", "Chad", "Karen"]
lastNames: list = ["Crusher", "Mallet", "Sjorborn", "Pancakes", "Smith"]


ENEMY = EnemyValues()

PLAYER = PlayerValues()

SHOP = ShopValues()

    #     ROOT CREATION    #


# Create Tkinter window
window = tkinter.Tk()
window.title("Clicker RPG")

# Change Theme
appTheme = ttk.Style()
appTheme.theme_use('winnative')
appTheme.configure("red.Horizontal.TProgressbar", foreground='red', background='red')


    #       FUNCTIONS      #


def close():
    """close the main window"""
    window.destroy()


def print_console(text):
    """print value to the console"""
    consoleGUI.insert("end", f"{text}\n")
    consoleGUI.see("end")


def buy_strength():
    """Upgrade PLAYER.strength of the player"""
    if PLAYER.gold >= SHOP.strength_cost:
        PLAYER.gold -= SHOP.strength_cost
        SHOP.strength_cost = round(SHOP.strength_cost * 1.5)
        PLAYER.strength += 1
        goldLabel["text"] = f"Gold: {PLAYER.gold}"
        upgradeStrengthCost["text"] = f"{SHOP.strength_cost}"
        statsStrength["text"] = f"Strength: {PLAYER.strength}"

        print_console("Strength upgraded.\n")

    else:
        print_console("Insufficient Gold.\n")


def buy_allies():
    """Hire allies"""
    if PLAYER.gold >= SHOP.allies_cost:
        PLAYER.gold -= SHOP.allies_cost
        SHOP.allies_cost = round(SHOP.allies_cost * 2)
        PLAYER.allies += 1
        goldLabel["text"] = f"Gold: {PLAYER.gold}"
        upgradeAlliesCost["text"] = f"{SHOP.allies_cost}"
        statsAllies["text"] = f"Allies: {PLAYER.allies}"

        print_console("Ally hired.\n")

    else:
        print_console("Insufficient Gold.\n")


# Function to kill enemy
def kill():
    """When enemy dies"""
    random_multiplier = randint(1, 3)
    gold_gain = round((ENEMY.health / 5) * random_multiplier)
    PLAYER.gold += gold_gain
    PLAYER.kill_count += 1
    print_console(f"{ENEMY.name} Killed\nReceived {gold_gain} Gold!\n")

    ENEMY.reset()

    if ENEMY.name == PLAYER.name:
        print_console("You found yourself!\n")

    healthBar.config(maximum=ENEMY.health, value=ENEMY.health)
    goldLabel["text"] = f"Gold: {PLAYER.gold}"

    statsKillCount["text"] = f"Kills: {PLAYER.kill_count}"


# Function to deal "ally damage" every second
def allies_attack():
    """Ally damage loop"""
    ENEMY.health_current -= PLAYER.allies * PLAYER.strength
    healthBar["value"] = ENEMY.health_current

    # If enemy dies
    if healthBar["value"] <= 0:
        kill()

    healthNumber.config(text=f"{ENEMY.health_current}/{ENEMY.health}")
    # Continue the loop
    window.after(1000, allies_attack)


def critical_hit():
    """critical hit math"""
    crit: int = randint(1, 100)
    return bool(crit <= PLAYER.crit_chance)


# Function to deal damage per click
def attack():
    """Player damage per click"""

    if critical_hit():
        ENEMY.health_current -= PLAYER.strength * 2
        print_console(f"Critical hit on {ENEMY.name}!\n")
    else:
        ENEMY.health_current -= PLAYER.strength

    healthBar["value"] = ENEMY.health_current

    # If enemy dies
    if ENEMY.health_current <= 0:
        kill()

    healthNumber.config(text=f"{ENEMY.health_current}/{ENEMY.health}")

    #    PANEL CREATION    #


# Config column and row size + sizing
window.columnconfigure([0, 1, 2], weight=1, minsize=285)
window.rowconfigure(0, weight=1, minsize=570)

# Add "Panels"
leftPanel = tkinter.Frame(window, bg="#1e1e1e", padx=5, pady=10)
leftPanel.grid(sticky="ns")

middlePanel = tkinter.Frame(window, bg="#1e1e1e", padx=5, pady=10)
middlePanel.grid(sticky="ns", column=1, row=0)

rightPanel = tkinter.Frame(window, bg="#1e1e1e", padx=5, pady=10)
rightPanel.grid(sticky="ns", column=2, row=0)

    #   LEFT PANEL ASSETS  #


# Display player statistics
statsTitle = tkinter.Label(leftPanel,
                           text="Statistics",
                           bg="#1e1e1e", fg="#f1f1f1",
                           font=("System", 20))
statsTitle.grid(pady=(50, 20))

statsName = tkinter.Label(leftPanel,
                          text=PLAYER.name,
                          bg="#1e1e1e", fg="#f1f1f1",
                          font="System")
statsName.grid(row=1, pady=(0, 30))

statsStrength = tkinter.Label(leftPanel,
                              text=f"Strength: {PLAYER.strength}",
                              bg="#1e1e1e", fg="#f1f1f1",
                              height=2, width=20,
                              font=("System", 12))
statsStrength.grid(row=2)

statsAllies = tkinter.Label(leftPanel,
                            text=f"Allies: {PLAYER.allies}",
                            bg="#1e1e1e", fg="#f1f1f1",
                            height=2, width=20,
                            font=("System", 12))
statsAllies.grid(row=3)

statsKillCount = tkinter.Label(leftPanel,
                               text=f"Kills: {PLAYER.kill_count}",
                               bg="#1e1e1e", fg="#f1f1f1",
                               height=2, width=20,
                               font=("System", 12))
statsKillCount.grid(row=4)

console = tkinter.Frame(leftPanel,
                        bg="#1e1e1e",
                        pady=30)
console.grid(row=10, column=0)

consoleGUI = tkinter.Text(console,
                          bg="#0e0e0e", fg="#f1f1f1",
                          height=15, width=30,
                          font="System")
consoleGUI.grid(row=0, sticky="s")

consoleScrollbar = tkinter.Scrollbar(console)
consoleScrollbar.grid(row=0, column=1, sticky='ns')

consoleGUI.config(yscrollcommand=consoleScrollbar.set)
consoleScrollbar.config(command=consoleGUI.yview)

    #  MIDDLE PANEL ASSETS #


# Create new frame for health values
healthFrame = tkinter.Frame(middlePanel, bg="#1e1e1e")
healthFrame.grid()

# Display enemy health bar
healthBar = ttk.Progressbar(healthFrame,
                            mode='determinate',
                            style="red.Horizontal.TProgressbar",
                            maximum=ENEMY.health,
                            value=ENEMY.health, length=200)

healthBar.grid(row=0)

# Display enemy health number
healthNumber = tkinter.Label(healthFrame,
                             text=f"{ENEMY.health_current}/{ENEMY.health}",
                             bg="#1e1e1e", fg="#f1f1f1",
                             width=5,
                             padx=10, pady=50,
                             font=("System", 20))
healthNumber.grid(row=0, column=1)

# Display enemy
enemy = tkinter.Button(middlePanel,
                       height=15, width=20,
                       pady=10,
                       command=attack)
enemy.grid(row=1)

enemyName = tkinter.Label(middlePanel,
                          text=ENEMY.name,
                          bg="#1e1e1e", fg="#f1f1f1",
                          font="System")
enemyName.grid(row=2, pady=(0, 30))

    #  RIGHT PANEL ASSETS  #


# Display PLAYER.gold value label
goldLabel = tkinter.Label(rightPanel,
                          text=f"Gold: {PLAYER.gold}",
                          bg="#1e1e1e", fg="#f1f1f1",
                          pady=50,
                          font=("System", 20))
goldLabel.grid(row=1)

# Strength upgrade button
upgradeStrength = tkinter.Button(rightPanel,
                                 text="Upgrade your strength!",
                                 bg="#0e0e0e", fg="#f1f1f1",
                                 height=2, width=20,
                                 command=buy_strength,
                                 font=("System", 12))
upgradeStrength.grid(row=2)

upgradeStrengthCost = tkinter.Label(rightPanel,
                                    text=SHOP.strength_cost,
                                    bg="#1e1e1e", fg="#f1f1f1",
                                    padx=10,
                                    font=("System", 12))
upgradeStrengthCost.grid(row=2, column=1)

# Allies upgrade button
upgradeAllies = tkinter.Button(rightPanel,
                               text="Hire new allies!",
                               bg="#0e0e0e", fg="#f1f1f1",
                               height=2, width=20,
                               font=("System", 12),
                               command=buy_allies)
upgradeAllies.grid(row=3)

upgradeAlliesCost = tkinter.Label(rightPanel,
                                  text=SHOP.allies_cost,
                                  bg="#1e1e1e", fg="#f1f1f1",
                                  padx=10,
                                  font=("System", 12))
upgradeAlliesCost.grid(row=3, column=1)

    #     INITIATE ROOT    #


# Change window size and color
window.geometry("900x600")
window.config(bg='#1e1e1e')

# Initiate window
window.after(1000, allies_attack)
window.mainloop()
