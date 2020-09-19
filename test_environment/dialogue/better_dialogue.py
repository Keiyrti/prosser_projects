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
                                   justify='center',
                                   cursor="hand2")
        self.speed_1x.place(anchor='sw', relx=0.5, rely=0.95, x=-400, y=-200)

        self.speed_2x = tkin.Label(self.master,
                                   bg=self.secondary_color, fg=self.text_color,
                                   image=self._invis_pic,
                                   compound='c',
                                   width=30, height=10,
                                   text='2x',
                                   justify='center',
                                   cursor="hand2")
        self.speed_2x.place(anchor='sw', relx=0.5, rely=0.95, x=-370, y=-200)

        self.speed_x: list = [self.speed_1x, self.speed_2x]

        self.locked = False

        self.text_box.bind('<Button-1>', self.click_event)
        self.master.bind('<Return>', self.hyper_action)

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
                self.char_max = 0
                self.items_max = len(value) - 1
                self.speed = 50
                self.items_completed = False
                self.bind = False
                self.skip = False
                self.printing = None
                self.hyper = False
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

        if self.hyper == True:
            self.hyper_action()
        else:
            self.action()

    def click_event(self, event=None):
        if self.items_completed == True:
            pass
        else:
            self.skip = True
            if self.printing != None:
                self.master.after_cancel(self.printing)
                self.printing = None
        self.action()

    def action(self, event=None):
        print(f"Current Item: {self.items_index}")
        print(f"Max Items: {self.items_max}")
        if self.items == [] or self.locked == True or self.items_index > self.items_max:
            pass
        elif self.items_completed == True:
            self.skip = False
            self.update()
        elif self.skip == True:
            _item = self.items[self.items_index]

            if isinstance(_item, str):
                self.char_max = len(_item)
                self.bind = False
                self.print()
            elif isinstance(_item, float):
                self.update()
            elif isinstance(_item, int):
                self.speed = _item
                self.update()
        else:
            _item = self.items[self.items_index]

            if isinstance(_item, str):
                self.char_max = len(_item)
                if self.bind == False:
                    self.text = ''
                else:
                    self.bind = False
                self.print()
            elif isinstance(_item, float):
                _pause = round(_item)
                if self.skip == True:
                    self.update()
                else:
                    self.printing = self.master.after(_pause, self.update)
            elif isinstance(_item, int):
                self.speed = _item
                self.update()

    def hyper_action(self, event=None):
        self.hyper = True
        self.skip = True
        if self.printing != None:
            self.master.after_cancel(self.printing)
            self.printing = None
        for _items in self.items:
            if self.items == [] or self.locked == True or self.items_index > self.items_max:
                self.hyper = False
                self.skip = False
            elif self.items_completed == True:
                self.update()
            elif self.hyper == True:
                _item = self.items[self.items_index]
                if isinstance(_item, str):
                    self.char_max = len(_item)
                    if self.bind == True:
                        self.bind = False
                    else:
                        self.text = ''
                    self.print()
                elif isinstance(_item, float):
                    self.update()
                elif isinstance(_item, int):
                    self.speed = _item
                    self.update()

    def print(self):
        _speed = self.speed

        print(f"Max Char: {self.char_max}")
        print(f"Current Char: {self.char_index}")
        if self.char_index >= self.char_max:
            self.printing = None
            self.items_completed = True
        elif self.items[self.items_index][self.char_index] == '+':
            print('PLUS!')
            self.bind = True
            self.update()
        else:
            self.text_box['text'] += self.items[self.items_index][self.char_index]
            self.char_index += 1
            if self.skip == True:
                self.print()
            else:
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

    _items = ["This is a test!",
               "Is this working?",
               "What happens when I tweak the speed a bit?",
               100, 'It seems that I made it a little too slow...',
               10, 'WOAH WOAH WOAH. TOO FAST!',
               50, "I think it's calmed down now.",
               "How about large chunks of text?",
               25, "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
               + " In tincidunt id mauris id consequat. Nulla interdum,"
               + " nibh eu interdum ultrices, nunc est dapibus mi,"
               + " accumsan porta leo sapien non nulla."
               + " Aenean bibendum odio vel venenatis feugiat."
               + " Praesent cursus velit sed turpis sagittis ornare."
               + " Suspendisse dictum interdum diam ac scelerisque."
               + " Nunc mauris turpis, volutpat id orci lobortis,"
               + " porttitor eleifend lorem."
               + " Nam finibus eros ac justo convallis accumsan."
               + " Sed sed rutrum risus. Etiam eros nisl,"
               + " aliquet id dapibus eu, cursus eu odio. Vestibulum congue,"
               + " velit eu porta viverra, neque neque aliquam arcu,"
               + " eget ultricies ante risus quis sapien."
               + " Cras dapibus enim non est fringilla fringilla.\n\n"
               + "Maecenas et nisl eros."
               + " Fusce et lacus sit amet ex porta blandit vitae id dui."
               + " Fusce quis mauris vitae dolor sollicitudin imperdiet."
               + " In sed ante vel sapien sagittis iaculis."
               + " Cras ut egestas nisi. Nullam eu dignissim leo."
               + " Aliquam sem ipsum, laoreet vel nibh in,"
               + " mattis dictum sapien.",
               50, "Try clicking around here to create a label!",
               "Wow. It worked...",
               "Maybe click again to destroy it?",
               "And there it goes!",
               "Now let's test if unlocking works!",
               "Try to click here!",
               "Only worked after you unlocked it, right?",
               "AND THAT'S A WRAP!",
               "Call it a flex?"]

    _dialogue.items = _items

    root.mainloop()
