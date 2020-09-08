"""
Idle Clicker Remastered.

By Jack, Dane, and Autum
"""

import tkinter
import tkinter.ttk as ttk

from random import randint

from time import sleep

class PlayerValues(dict):
    """Define values and modules for the PLAYER object."""
    def __init__(self):
        """Initialize PLAYER with a random name and starting values."""
        self.random_name()
        self["strength"] = 5
        self["crit_chance"] = 5
        self["skill_one_level"] = 1
        self["stage"] = 1
        self["skill_one"] = False
        self["skill_two"] = False
        self["skill_three"] = False

    def random_name(self):
        """Give PLAYER a random name."""
        self["name"] = (f"{first_name[randint(0, len(first_name) - 1)]}"
                        + f" {last_name[randint(0, len(last_name) - 1)]}")

    def critical_hit(self):
        """Return value for critical hits."""
        _crit = randint(1,100)
        if _crit <= self["crit_chance"]:
            return True
        return False

    def attack(self):
        """Return damage values."""
        if not self["skill_one"]:
            if not self.critical_hit():
                return self["strength"]
            return self["strength"] * 2

        if not self.critical_hit():
            return self["strength"] * 2
        return self["strength"] * 3


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

    def random_health(self):
        """Give ENEMY a random health value."""
        self["health_max"] = round(randint(40,50) * PLAYER["stage"] / 10)
        self["health"] = self["health_max"]

first_name: list = ["Jack", "Dane", "Autum"]
last_name: list = ["Kiv", "Claus", "San"]

PLAYER = PlayerValues()
ENEMY = EnemyValues()

def attack(event):
    ENEMY['health'] -= PLAYER.attack()
    enemy_health_number['text'] = (f"{ENEMY['health']}"
                                   + f"/{ENEMY['health_max']}")


root = tkinter.Tk()
root.title("Endless Expansion V1.0")

root.grid_columnconfigure([0,2],
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
                            text = PLAYER["name"],
                            font = ("System", 18))
player_name.grid(row=0,column=0,
                 sticky="nsew")


player_stats = tkinter.Frame(left_panel,
                             bg="#2e2e2e")
player_stats.grid(row=1,column=0,
                  padx=20, pady=10,
                  sticky="nsew")

player_skills = tkinter.Frame(left_panel,
                             bg="#1e1e1e")
player_skills.grid(row=2, column=0,
                   sticky="nsew", padx=15)

player_skills.grid_columnconfigure([0,1,2],
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
                                  width=5, height = 2,
                                  text="One")
player_skill_one.grid(row=1, column=0,
                      padx=5, pady=5, sticky='ew')

player_skill_two = tkinter.Button(player_skills,
                                  width=5, height = 2,
                                  text="Two")
player_skill_two.grid(row=1, column=1,
                      padx=5, pady=5, sticky='ew')

player_skill_three = tkinter.Button(player_skills,
                                  width=5, height = 2,
                                  text="Three")
player_skill_three.grid(row=1, column=2,
                      padx=5, pady=5, sticky='ew')

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
enemy_health.grid(row=0,column=0)


enemy_health_bar = ttk.Progressbar(enemy_health,
                                   mode="determinate",
                                   max=ENEMY["health_max"],
                                   value=ENEMY["health"],
                                   length=300)
enemy_health_bar.grid(row=0,column=0)



enemy_health_number = tkinter.Label(enemy_health,
                                    bg="#1e1e1e",
                                    fg="#f1f1f1",
                                    text=(f"{ENEMY['health']}"
                                          + f"/{ENEMY['health_max']}"),
                                    font=("System", 30))
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
console_window.grid(row=0, column=0, sticky='nsew', ipadx=5)

console_scrollbar = tkinter.Scrollbar(console)
console_scrollbar.grid(row=0, column=1, sticky="ns")

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
                            text = "Shop",
                            font = ("System", 18))
shop_name.grid(row=0,column=0,
                 sticky="nsew")

shop_stats = tkinter.Frame(right_panel,
                             bg="#2e2e2e")
shop_stats.grid(row=1,column=0,
                  padx=20, pady=10,
                  sticky="nsew")

shop_allies = tkinter.Frame(right_panel,
                          bg="#2e2e2e")
shop_allies.grid(row=2,column=0,
               padx=20, pady=10,
               sticky="nsew")

shop_skills = tkinter.Frame(right_panel,
                           bg="#2e2e2e")
shop_skills.grid(row=3,column=0,
                padx=20, pady=(10,20),
                sticky="nsew")

root.geometry("800x600")
root.mainloop()
