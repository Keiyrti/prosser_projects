"""
Idle Clicker Remastered.

By Jack, Dane, and Autum
"""


# IMPORTS #


import tkinter
import tkinter.ttk as ttk

import datetime
from random import randint
import pytz




# CLASSES #


# Create classes to store information. Object-orientated programming.
# Using these, we can ditch global variables and easily create fuctions that
# acton itself as well as create multiple of them without much issue.
class PlayerValues(dict):
    """Define values and modules for the PLAYER object."""

    def __init__(self):
        """Initialize PLAYER with a random name and starting values."""
        self.random_name()
        # self['name'] = "Belle Delphine"
        self["strength"] = 5
        self["crit_chance"] = 5

        self["gold"] = 0

        self["peasants"] = 0
        self["knights"] = 0
        self["adventurers"] = 0
        self["heroes"] = 0

        self["skill_one_level"] = 0
        self["skill_two_level"] = 0
        self["skill_three_level"] = 0

        self["skill_one"] = False
        self["skill_two"] = False
        self["skill_three"] = False

        self["stage"] = 1

    def random_name(self):
        """Give PLAYER a random name."""
        self["name"] = (f"{first_name[randint(0, len(first_name) - 1)]}"
                        + f" {last_name[randint(0, len(last_name) - 1)]}")

    def critical_hit(self):
        """Return value for critical hits."""
        _crit = randint(1, 100)
        if _crit <= self["crit_chance"]:
            return True
        return False

    def attack(self):
        """Return damage values."""
        if not self["skill_one"]:
            if not self.critical_hit():
                return self["strength"]
            print_console(crit_message(PLAYER["name"]))
            return self["strength"] * 2

        if not self.critical_hit():
            return self["strength"] * 2
        return self["strength"] * 3

    def allies_attack(self):
        """Return allies damage values."""
        _damage: int = 0
        _damage += self["peasants"] * 2
        _damage += self["knights"] * 10
        _damage += self["adventurers"] * 25
        _damage += self["heroes"] * 100
        if self['name'] == "Jotaro Joestar":
            _damage += self["strength"]
        return _damage

    def gold_increase(self, health):
        """Increase player's gold depending on enemy health."""
        _gold_gain = round((health / 5) * 2)
        self['gold'] += _gold_gain

        return _gold_gain


class EnemyValues(dict):
    """Define values and modules for the ENEMY object."""

    def __init__(self):
        """Initialize ENEMY with a random name."""
        self.random_name()
        self.random_health()

    def random_name(self):
        """Give ENEMY a random name."""
        self["name"] = (f"{first_name[randint(0, len(first_name) - 1)]}"
                        + f" {last_name[randint(0, len(last_name) - 1)]}")
        if self['name'] == 'Dio Brando' and (time.now(timezone).hour < 6
            or time.now(timezone).hour > 20):

            self['name'] = 'DIO'

    def random_health(self):
        """Give ENEMY a random health value."""
        self["health_max"] = round(randint(40, 50) * PLAYER["stage"] / 10)
        self["health"] = self["health_max"]


# VARIABLES #


first_name: list = ["Jack", "Dane", "Autum", "Jotaro", "Belle", "Dio"]
last_name: list = ["Kiv", "Claus", "San", "Joestar", "Delphine", "Brando"]

PLAYER = PlayerValues()
ENEMY = EnemyValues()

time = datetime.datetime
timezone = pytz.timezone('America/Kentucky/Louisville')
# timezone = pytz.timezone('Asia/Bangkok')

SECONDS: int = 0


# FUNCTIONS #


# Add functions for game logic
def print_console(value):
    """Print value to the console."""
    console_window.insert("end", f"{value}\n")
    console_window.see("end")


def crit_message(name):
    """Switch critical hit message depending on name."""
    switcher = {
        'Jotaro Joestar': "Ora ora ora!"
    }
    return switcher.get(name, "Critical hit!")


def enemy_update():
    """Update ENEMY screen values."""
    enemy_name['text'] = ENEMY['name']
    enemy_health_bar['max'] = ENEMY['health_max']
    enemy_health_bar['value'] = ENEMY['health']
    enemy_health_number['text'] = (f"{ENEMY['health']}"
                                   + f"/{ENEMY['health_max']}")


def player_update():
    """Update PLAYER screen values."""
    player_name['text'] = PLAYER['name']
    player_gold_value['text'] = PLAYER['gold']
    player_strength_value['text'] = PLAYER['strength']
    player_dexterity_value['text'] = PLAYER['crit_chance']


def death():
    """Activate when enemy dies to reset values."""
    if ENEMY['health'] > 0:
        pass

    elif ENEMY['name'] == 'DIO':

        ENEMY['health'] = ENEMY['health_max']
        enemy_update()
        _quote: dict = {0: "Oh? You're approaching, me?", 1: "MUDA MUDA!", 2:"ZA WARUDO!"}
        print_console(_quote[randint(0, len(_quote)-1)])

    else:
        print_console(f"{PLAYER.gold_increase(ENEMY['health_max'])} Gold Received.")

        ENEMY.random_name()
        ENEMY.random_health()
        enemy_update()
        PLAYER['stage'] += 1
    player_update()


def attack(event):
    """Activate when PLAYER clicks to damage ENEMY."""
    ENEMY['health'] -= PLAYER.attack()
    death()
    enemy_update()


def game_tick():
    """Store all loops."""
    global SECONDS
    SECONDS += 1
    if SECONDS > 3600:
        SECONDS = 0

    if PLAYER['name'] == 'Belle Delphine' and SECONDS % 60 == 0:
        _gold_gain = round(PLAYER['gold'] * .5)
        PLAYER['gold'] += _gold_gain
        print_console(f"Your patreons paid {_gold_gain} Gold!")

    ENEMY['health'] -= PLAYER.allies_attack()
    death()
    enemy_update()
    root.after(1000, game_tick)


# ROOT CREATION #


root = tkinter.Tk()
root.title("Endless Expansion V1.0")

root.grid_columnconfigure([0, 2],
                          weight=225,
                          minsize=225)
root.grid_columnconfigure(1,
                          weight=350,
                          minsize=350)
root.grid_rowconfigure(0,
                       weight=600,
                       minsize=600)


# CREATE PANELS #


left_panel = tkinter.Frame(root,
                           bg="#1e1e1e")
left_panel.grid(row=0, column=0,
                sticky="nsew")

middle_panel = tkinter.Frame(root,
                             bg="#1e1e1e")
middle_panel.grid(row=0, column=1,
                  sticky="nsew")

right_panel = tkinter.Frame(root,
                            bg="#1e1e1e")
right_panel.grid(row=0, column=2,
                 sticky="nsew")


# LEFT PANEL ASSETS #


left_panel.grid_columnconfigure(0,
                                weight=225,
                                minsize=225)
left_panel.grid_rowconfigure(0,
                             weight=75,
                             minsize=75)
left_panel.grid_rowconfigure(1,
                             weight=425,
                             minsize=425)
left_panel.grid_rowconfigure(2,
                             weight=100,
                             minsize=100)

player_name = tkinter.Label(left_panel,
                            bg="#1e1e1e",
                            fg="#f1f1f1",
                            text=PLAYER["name"],
                            font=("System", 18))
player_name.grid(row=0, column=0,
                 sticky="nsew")


player_stats = tkinter.Frame(left_panel,
                             bg="#2e2e2e")
player_stats.grid(row=1, column=0,
                  padx=20, pady=10,
                  sticky="nsew")

player_stats.grid_columnconfigure(0,
                                  weight=100,
                                  minsize=100)
player_stats.grid_columnconfigure(1,
                                  weight=125,
                                  minsize=125)

player_gold = tkinter.Label(player_stats,
                    bg="#2e2e2e",
                    fg="#f1f1f1",
                    text="Gold",
                    font=("System", 16))
player_gold.grid(row=0, column=0,
                 padx=10, pady=10,
                 sticky="w")
player_gold_value = tkinter.Label(player_stats,
                                  bg="#2e2e2e",
                                  fg="#f1f1f1",
                                  text=PLAYER['gold'],
                                  font=("System", 12))
player_gold_value.grid(row=0, column=1,
                       padx=0, pady=10,
                       sticky="w")

player_strength = tkinter.Label(player_stats,
                                bg="#2e2e2e",
                                fg="#f1f1f1",
                                text="Strength",
                                font=("System", 16))
player_strength.grid(row=1, column=0,
                     padx=10, pady=(10, 5),
                     sticky="w")
player_strength_value = tkinter.Label(player_stats,
                                      bg="#2e2e2e",
                                      fg="#f1f1f1",
                                      text=PLAYER['strength'],
                                      font=("System", 12))
player_strength_value.grid(row=1, column=1,
                           padx=0, pady=(10, 5),
                           sticky="w")

player_dexterity = tkinter.Label(player_stats,
                                 bg="#2e2e2e",
                                 fg="#f1f1f1",
                                 text="Dexterity",
                                 font=("System", 16))
player_dexterity.grid(row=2, column=0,
                      padx=10, pady=(5, 10),
                      sticky="w")
player_dexterity_value = tkinter.Label(player_stats,
                                       bg="#2e2e2e",
                                       fg="#f1f1f1",
                                       text=PLAYER['crit_chance'],
                                       font=("System", 12))
player_dexterity_value.grid(row=2, column=1,
                            padx=0, pady=(5, 10),
                            sticky="w")



player_skills = tkinter.Frame(left_panel,
                              bg="#1e1e1e")
player_skills.grid(row=2, column=0,
                   sticky="nsew", padx=15)

player_skills.grid_columnconfigure([0, 1, 2],
                                   weight=75,
                                   minsize=25)
player_skill_one_bar = ttk.Progressbar(player_skills,
                                       mode="determinate",
                                       max=60,
                                       value=30,
                                       length=40)
player_skill_one_bar.grid(row=0, column=0,
                          padx=5, pady=5, sticky='ew')

player_skill_one = tkinter.Button(player_skills,
                                  width=5, height=2,
                                  bg="#2e1e1e", fg="#f1f1f1",
                                  text="Athena",
                                  font="System")
player_skill_one.grid(row=1, column=0,
                      padx=5, pady=5, sticky='ew')

player_skill_two = tkinter.Button(player_skills,
                                  width=5, height=2,
                                  bg="#2e1e1e", fg="#f1f1f1",
                                  text="Midas",
                                  font="System")
player_skill_two.grid(row=1, column=1,
                      padx=5, pady=5, sticky='ew')

player_skill_three = tkinter.Button(player_skills,
                                    width=5, height=2,
                                    bg="#2e1e1e", fg="#f1f1f1",
                                    text="Ares",
                                    font="System")
player_skill_three.grid(row=1, column=2,
                        padx=5, pady=5,
                        sticky='ew')

player_skill_two_bar = ttk.Progressbar(player_skills,
                                       mode="determinate",
                                       max=60,
                                       value=30,
                                       length=40)
player_skill_two_bar.grid(row=0, column=1,
                          padx=5, pady=5, sticky='ew')

player_skill_three_bar = ttk.Progressbar(player_skills,
                                         mode="determinate",
                                         max=60,
                                         value=30,
                                         length=40)
player_skill_three_bar.grid(row=0, column=2,
                            padx=5, pady=5, sticky='ew')


# MIDDLE PANEL ASSETS #


middle_panel.grid_columnconfigure(0,
                                  weight=225,
                                  minsize=225)
middle_panel.grid_rowconfigure(0,
                               weight=75,
                               minsize=75)
middle_panel.grid_rowconfigure(1,
                               weight=300,
                               minsize=300)
middle_panel.grid_rowconfigure(2,
                               weight=225,
                               minsize=225)
enemy_health = tkinter.Frame(middle_panel,
                             bg="#1e1e1e")
enemy_health.grid(row=0, column=0)


enemy_health_bar = ttk.Progressbar(enemy_health,
                                   mode="determinate",
                                   length=300)
enemy_health_bar.grid(row=0, column=0)


enemy_health_number = tkinter.Label(enemy_health,
                                    bg="#1e1e1e",
                                    fg="#f1f1f1",
                                    font=("System", 20))
enemy_health_number.grid(row=1, column=0)
enemy_health.lower(belowThis=enemy_health_bar)

enemy = tkinter.Frame(middle_panel,
                      bg="#1e1e1e")

enemy.grid(row=1, column=0)

enemy_name = tkinter.Label(enemy,
                           bg="#1e1e1e",
                           fg="#f1f1f1",
                           text=ENEMY["name"],
                           font=("System", 18))
enemy_name.grid(row=0, column=0)
enemy_body = tkinter.Frame(enemy,
                           bg="#2e1e1e",
                           width=200,
                           height=300)
enemy_body.grid(row=1, column=0)

middle_panel.bind("<Button-1>", attack)
enemy.bind("<Button-1>", attack)
enemy_name.bind("<Button-1>", attack)
enemy_body.bind("<Button-1>", attack)

console = tkinter.Frame(middle_panel,
                        bg="#1e1e1e")
console.grid(row=2, column=0, sticky='nesw', pady=10)
console.grid_columnconfigure(0, weight=1)
console.grid_columnconfigure(1, weight=0)

console_window = tkinter.Text(console,
                              bg="#1e1e1e", fg="#f1f1f1",
                              width=40, height=12,
                              font="System")
console_window.grid(row=0, column=0, sticky='nsew')

console_scrollbar = tkinter.Scrollbar(console)
console_scrollbar.grid(row=0, column=1, sticky="nsew")

console_window.config(yscrollcommand=console_scrollbar.set)
console_scrollbar.config(command=console_window.yview)


# RIGHT PANEL ASSETS #


right_panel.grid_columnconfigure(0,
                                 weight=225,
                                 minsize=225)
right_panel.grid_rowconfigure(0,
                              weight=75,
                              minsize=75)
right_panel.grid_rowconfigure(1,
                              weight=116,
                              minsize=116)
right_panel.grid_rowconfigure(2,
                              weight=232,
                              minsize=232)
right_panel.grid_rowconfigure(3,
                              weight=175,
                              minsize=175)


shop_name = tkinter.Label(right_panel,
                          bg="#1e1e1e",
                          fg="#f1f1f1",
                          text="Shop",
                          font=("System", 18))
shop_name.grid(row=0, column=0,
               sticky="nsew")

shop_stats = tkinter.Frame(right_panel,
                           bg="#2e2e2e")
shop_stats.grid(row=1, column=0,
                padx=20, pady=10,
                sticky="nsew")

shop_allies = tkinter.Frame(right_panel,
                            bg="#2e2e2e")
shop_allies.grid(row=2, column=0,
                 padx=20, pady=10,
                 sticky="nsew")

shop_skills = tkinter.Frame(right_panel,
                            bg="#2e2e2e")
shop_skills.grid(row=3, column=0,
                 padx=20, pady=(10, 20),
                 sticky="nsew")
# INITIATE ROOT #
enemy_update()
player_update()

root.geometry("800x600")
root.after(1000, game_tick)
root.mainloop()
