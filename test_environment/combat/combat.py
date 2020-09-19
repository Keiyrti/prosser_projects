"""Combat system."""

import tkinter as tkin

class health_bar(tkin.Frame):
    def __init__(self, master, cnf={}, x=0, y=5, relx=0.0, rely=0.0, **kw):
        tkin.Frame.__init__(self, master, cnf)
        self.width = int(self['width'])
        self.height = int(self['height'])
        self.place(anchor='sw', x=x, y=y, relx=relx, rely=rely)

        self._invis_pic = tkin.PhotoImage(width=1, height=1)


    def init_health_bar(self, cnf={}, health_max=100):
        self.health_bar = tkin.Frame(self, cnf)
        self.health_bar['width'] = self.width - 10
        self.health_bar['height'] = self.height - 10
        self.health_bar.place(anchor='w', x=5, rely=0.5)
        self.start_width = int(self.health_bar['width'])

        _health = round(health_max / health_max * self.start_width)
        self.value = tkin.StringVar()
        self.value.set(_health)

        self.value.trace("w", self._update)

    def _update(self, *args):
        self.health_bar['width'] = self.value.get()
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
            self.enemy1_object.bind("<Button-1>", self.enemy_select)
            if count >= 2:
                self.enemy2_object = self.enemy(self.enemy_frame, 275)
                self.enemy2_object.place(anchor='s', x=275, rely=0.4)
                self.enemy2_object.bind("<Button-1>", self.enemy_select)
            if count >= 3:
                self.enemy3_object = self.enemy(self.enemy_frame, 150, 0.7)
                self.enemy3_object.place(anchor='s', x=150, rely=0.7)
                self.enemy3_object.bind("<Button-1>", self.enemy_select)
            if count == 4:
                self.enemy4_object = self.enemy(self.enemy_frame, 300, 0.7)
                self.enemy4_object.place(anchor='s', x=300, rely=0.7)
                self.enemy4_object.bind("<Button-1>", self.enemy_select)

            self.selected_enemy = 'enemy1'
            self.selected_crosshair = tkin.Label(self.enemy_frame,
                                                 bg='#f1f1f1',
                                                 image=self._invis_pic,
                                                 compound='c',
                                                 width=20, height=20)
            self.selected_enemy = self.enemy1_object
            self.selected_crosshair.place(x=self.enemy1_object.x - 30, rely=self.enemy1_object.y, y=-90)






    def enemy_select(self, event):
        self.selected_enemy = event.widget
        self.selected_crosshair.place(x=event.widget.x - 30, rely=event.widget.y, y=-90)

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
                     cnf={}, **kw):
            tkin.Label.__init__(self, master, cnf)

            self._invis_pic = tkin.PhotoImage(width=1, height=1)

            self.health = 100
            self.strength = 6
            self.dexterity = 6
            self.agility = 6
            self.defense = 6

            self['bg'] = '#f1f1f1'
            self['width'] = 80
            self['height'] = 100
            self['image'] = self._invis_pic
            self['compound'] = 'c'

            _health_bar_config = {'width': 80, 'height': 25, 'bg':'#654321'}
            _inner_bar_config = {'bg':'#68bb4e'}
            self.health_bar = health_bar(master, _health_bar_config, **{'relx': 0.5, 'rely':0.5})
            self.health_bar.init_health_bar(_inner_bar_config)

        def attack(self, enemy=None, master=None):
            if enemy == None:
                pass
            else:
                enemy.health -= self.strength
                enemy.update()

                if enemy.health < 0:
                    enemy.health_bar.destroy()
                    enemy.destroy()
                    master.selected_crosshair.place_forget()
                    master.selected_enemy = None

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

            self.health_max = 100
            self.health = self.health_max

            _health_bar_config = {'width': 60, 'height': 26, 'bg':'#654321'}
            _inner_bar_config = {'bg':'#dd3a2a'}
            self.health_bar = health_bar(master, _health_bar_config, **{'x':self.x, 'rely':self.y})
            self.health_bar.init_health_bar(_inner_bar_config)
        def update(self):
            _health = round(self.health / self.health_max * self.health_bar.start_width)
            self.health_bar.value.set(_health)

# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Combat Prototype")
    root.geometry("1600x900")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#5e5e5e'

    # Import CombatWindow
    _combat = CombatWindow(root)
    _combat.place_enemies(4)

                                                                                # INITIALIZE ROOT #
    root.mainloop()
