"""Combat system."""

import tkinter as tkin
import text_dialogue as txt_

                                                                                # Define the Combat Window class
class CombatWindow():
    """Class for easily implementing turnbased combat."""


                                                                                # INITIALIZE SETTINGS #
    def __init__(self, master):
        """Create Combat Window."""
        # Set master
        self.master = master

        self._invis_pic = tkin.PhotoImage(width=1, height=1)

        # Create combat frame
        self.combat_frame = tkin.Frame(master,
                                       bg="#282828",
                                       width=1000,
                                       height=400)

        self.combat_frame.place(anchor="center",
                                relx=0.5, rely=0.4)

        # Create options frame
        self.options_frame = tkin.Frame(self.combat_frame,
                                       bg="#654321")
        self.options_frame.place(width=225, height=400)

        self.options_frame_foreground = tkin.Frame(self.options_frame,
                                                   bg='#2e2e2e')
        self.options_frame_foreground.place(anchor='center',
                                 relx=0.5, rely=0.5,
                                 width=205, height=380)

        self.options_attack = tkin.Button(self.options_frame,
                                          width=180, height=50,
                                          image=self._invis_pic,
                                          compound='c',
                                          text='Attack',
                                          font=('System', 20),
                                          command=lambda: self.player_object.attack(self.selected_enemy, self))
        self.options_attack.grid(pady=(20, 10), padx=20, sticky='ew')

        self.options_spells = tkin.Button(self.options_frame,
                                          width=180, height=50,
                                          image=self._invis_pic,
                                          compound='c',
                                          text='Spells',
                                          font=('System', 20))
        self.options_spells.grid(row=1, pady=0, padx=20, sticky='ew')

        # Create player frame
        self.player_frame = tkin.Frame(self.combat_frame,
                                       bg=self.combat_frame['bg'])
        self.player_frame.place(x=225,
                                width=225, height=400)

        # Create middle frame
        self.middle_frame = tkin.Frame(self.combat_frame,
                                       bg=self.combat_frame['bg'])
        self.middle_frame.place(x=450,
                                width=100, height=400)

        # Create enemy frame
        self.enemy_frame = tkin.Frame(self.combat_frame,
                                       bg=self.combat_frame['bg'])
        self.enemy_frame.place(x=550,
                               width=450, height=400)

        self.place_player()

    def place_player(self):
        self.player_object = self.player(self.player_frame)
        self.player_object.place(anchor='s', relx=0.5, rely=0.5)

    def place_enemies(self, count=1):
        if count != 0:
            self.enemy1_object = self.enemy(self.enemy_frame)
            self.enemy1_object.place(anchor='s', x=125, rely=0.4)
            self.enemy1_object.bind("<Button-1>", lambda x: self.enemy_select(self.enemy1_object))
            if count >= 2:
                self.enemy2_object = self.enemy(self.enemy_frame, 275)
                self.enemy2_object.place(anchor='s', x=275, rely=0.4)
                self.enemy2_object.bind("<Button-1>", lambda x: self.enemy_select(self.enemy2_object))
            if count >= 3:
                self.enemy3_object = self.enemy(self.enemy_frame, 150, 0.7)
                self.enemy3_object.place(anchor='s', x=150, rely=0.7)
                self.enemy3_object.bind("<Button-1>", lambda x: self.enemy_select(self.enemy3_object))
            if count == 4:
                self.enemy4_object = self.enemy(self.enemy_frame, 300, 0.7)
                self.enemy4_object.place(anchor='s', x=300, rely=0.7)
                self.enemy4_object.bind("<Button-1>", lambda x: self.enemy_select(self.enemy4_object))

            self.selected_enemy = 'enemy1'
            self.selected_crosshair = tkin.Label(self.enemy_frame,
                                                 bg='#f1f1f1',
                                                 image=self._invis_pic,
                                                 compound='c',
                                                 width=20, height=20)
            self.enemy_select(self.enemy1_object)






    def enemy_select(self, enemy=None):
        self.selected_enemy = enemy
        if enemy == None:
            pass
        else:
            self.selected_crosshair.place(x=enemy.x - 30, rely=enemy.y, y=-90)

    def text_update(self, text: str=None, text_box=None):
        if text == None:
            pass
        elif text_box == None:
            print(text)
        elif text_box.assets == None:
            _text = [text]
            text_box.import_assets(_text)
            text_box.skip()
        else:
            text_box.skip()
            text_box.assets.append(text)
            text_box.skip()


    class player(tkin.Label):

        def __init__(self, master,
                     health=100,
                     strength=6, dexterity=6,
                     agility=6, defense=6,
                     cnf={}, **kw):
            tkin.Label.__init__(self, master, cnf)

            self._invis_pic = tkin.PhotoImage(width=1, height=1)

            self.health = health
            self.strength = strength
            self.dexterity = dexterity
            self.agility = agility
            self.defense = defense

            self['bg'] = '#f1f1f1'
            self['width'] = 80
            self['height'] = 100
            self['image'] = self._invis_pic
            self['compound'] = 'c'

        def attack(self, enemy=None, master=None):
            if enemy == None:
                pass
            else:
                enemy.health -= self.strength
                enemy.update()
                _text = f'Player hits Enemy for {self.strength}!'
                master.text_update(_text, _dialogue)
                if enemy.health < 0:
                    master.selected_crosshair.place_forget()
                    master.enemy_select()
                    enemy.destroy()

    class enemy(tkin.Label):
        def __init__(self, master, x=125, y=0.4, cnf={}, **kw):
            tkin.Label.__init__(self, master, cnf)

            self._invis_pic = tkin.PhotoImage(width=1, height=1)

            self['bg'] = '#ff6961'
            self['fg'] = '#0e0e0e'
            self['width'] = 80
            self['height'] = 100
            self['image'] = self._invis_pic
            self['compound'] = 'c'

            self.x = x
            self.y = y

            self.health = 100

        def update(self):
            self['text'] = self.health

# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Combat Prototype")
    root.geometry("1600x900")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#d1d1d1'

    # Import CombatWindow
    _combat = CombatWindow(root)
    _combat.place_enemies(4)
    _dialogue = txt_.Dialogue(root)

                                                                                # INITIALIZE ROOT #
    root.mainloop()
