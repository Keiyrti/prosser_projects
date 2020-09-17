"""An Improved Dialogue System by Kirati Kiviniemi."""

import tkinter as tkin

class Dialogue:
    """Class for easily importing and printing strings."""

    main_color = "#654321"
    secondary_color = "#2e2e2e"
    text_color = "#f1f1f1"

    def __init__(self, master):
        """Set default parameters on initialization."""
        # Set master
        self.master = master

        self._invis_pic = tkin.PhotoImage(width=1, height=1)

        # Create dialogue frame
        self.bg_frame = tkin.Frame(master,
                                         bg=self.main_color,
                                         cursor="hand2")
        self.bg_frame.place(anchor='s', relx=0.5, rely=0.95,
                                  width=800, height=200)

        # Create dialogue box
        self.text_box = tkin.Label(self.bg_frame,
                                   bg=self.secondary_color, fg=self.text_color,
                                   font="System",
                                   wraplength=750,
                                   cursor="hand2")
        self.text_box.place(anchor='center', relx=0.5, rely=0.5,
                            width=780, height=180)

        self.text_counter = tkin.Label(self.master,
                                       bg=self.main_color , fg=self.text_color,
                                       image=self._invis_pic,
                                       compound='c',
                                       width=60, height=10,
                                       justify='right')

        self.speed_1x = tkin.Label(self.master,
                                   bg=self.main_color, fg=self.text_color,
                                   image=self._invis_pic,
                                   compound='c',
                                   width=30, height=10,
                                   text='1x',
                                   justify='left',
                                   cursor="hand2")
        self.speed_1x.place(anchor='sw', relx=0.5, rely=0.95, x=-400, y=-200)

        self.speed_2x = tkin.Label(self.master,
                                   bg=self.secondary_color, fg=self.text_color,
                                   image=self._invis_pic,
                                   compound='c',
                                   width=30, height=10,
                                   text='2x',
                                   justify='left',
                                   cursor="hand2")
        self.speed_2x.place(anchor='sw', relx=0.5, rely=0.95, x=-365, y=-200)

        self.speed_x: list = [self.speed_1x, self.speed_2x]

        self.locked = False

        self.text_box.bind('<Button-1>', self.skip)

    def __repr__(self):
        return "Dialogue Box Object"

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
        if name == 'items':
            if value != None:
                self.items_index = 0
                self.items_next = 1
                self.items_prev = -1
                self.char_index = 0
                self.items_max = len(value) - 1
                self.speed = 50
                self.items_completed = False
                self.bind = False
                self.skip_speed = False
                self.printing = None
                self.action()
            else:
                self.items = []
        elif name == 'text':
            self.text_box['text'] = value
        else:
            pass

    def update(self, **kw):
        self.items_index += 1
        self.items_next = self.items_index + 1
        self.items_prev = self.items_index - 1
        self.char_index = 0

        self.items_completed = False

        self.action()

    def skip(self, event):
        if self.items_completed == True:
            self.action()
        else:
            print("skip speed!")
            self.skip_speed = True

    def action(self, event=None):
        _item = self.items[self.items_index]
        if self.items == [] or self.locked == True or self.items_index > self.items_max:
            pass
        elif self.items_completed == True:
            self.update()
        elif isinstance(self.items[self.items_index], str):
            self.char_max = len(self.items[self.items_index])
            if self.bind == False:
                self.text = ''
            else:
                self.bind = False
            self.print()
        elif isinstance(_item, float):
            _pause = round(_item)
            self.printing = self.master.after(_pause, self.update)
        elif isinstance(self.items[self.items_index], int):
            self.speed = self.items[self.items_index]
            self.update()

    def print(self):
        _speed = self.speed
        if self.skip_speed == True:
            _speed = 0


        if self.char_index == self.char_max:
            self.printing = None
            self.items_completed = True
        elif self.items[self.items_index][self.char_index] == '+':
            self.items_completed = True
            self.bind = True
            self.update()
        else:
            self.text_box['text'] += self.items[self.items_index][self.char_index]
            self.char_index += 1
            self.printing = self.master.after(_speed, self.print)



if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Dialogue Prototype")
    root.geometry("1024x576")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#d1d1d1'
    root.text = "#1e1e1e"

    # Import Dialogue
    _dialogue = Dialogue(root)

    _items = ["So+", 300, "...+", 1000.0, 50, " Is this how it works?", "It all works!"]

    _dialogue.items = _items

    print(_dialogue.items_index)

    root.mainloop()
