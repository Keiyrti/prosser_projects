"""A Dialogue System Prototype."""

import tkinter as tkin

                                                                                # Define the Dialogue class
class Dialogue:
    """Class for easily adding speach dialogue."""

                                                                                # INITIALIZATION SETTINGS #
    def __init__(self, master):
        """Set default parameters on initialization."""
        # Set master
        self.master = master

        self._invis_pic = tkin.PhotoImage(width=1, height=1)

        # Create dialogue frame
        self.dialogue_frame = tkin.Frame(master,
                                         bg="#654321")
        self.dialogue_frame.place(anchor='s', relx=0.5, rely=0.95,
                                  width=800, height=200)

        # Create dialogue box
        self.dialogue_box = tkin.Label(self.dialogue_frame,
                                       bg="#2e2e2e", fg="#f1f1f1",
                                       font="System")
        self.dialogue_box.place(anchor='center', relx=0.5, rely=0.5,
                                width=780, height=180)

        # Create button display
        self.button_display = tkin.Label(self.dialogue_frame,
                                         bg="#2e2e2e", fg='#e1e1e1',
                                         text="LMB | Space",
                                         padx=5, pady=5,
                                         font="System")
        self.button_display.place(anchor='se', x=790, y=190)
        self.button_display.lift(aboveThis=self.button_display)

        self.paragraph_counter = tkin.Label(self.master,
                                            bg="#654321", fg="#f1f1f1",
                                            image=self._invis_pic,
                                            compound='c',
                                            padx=10,
                                            height=10,
                                            justify='right')

        self.speed_button_1x = tkin.Label(self.master,
                                          bg="#654321", fg="#f1f1f1",
                                          image=self._invis_pic,
                                          compound='c',
                                          width=30, height=10,
                                          text='1x',
                                          justify='left')
        self.speed_button_1x.place(anchor='sw', relx=0.5, rely=0.95, x=-400, y=-200)

        self.speed_button_2x = tkin.Label(self.master,
                                          bg="#2e2e2e", fg="#f1f1f1",
                                          image=self._invis_pic,
                                          compound='c',
                                          width=30, height=10,
                                          text='2x',
                                          justify='left')
        self.speed_button_2x.place(anchor='sw', relx=0.5, rely=0.95, x=-365, y=-200)

        self.speed_buttons: list = [self.speed_button_1x, self.speed_button_2x]

        # Bind LMB and SPACE to skipping dialogue
        self.dialogue_box.bind("<Button-1>", self.skip)
        self.dialogue_box.bind("<Shift-Button-1>", self.scroll_skip)
        self.master.bind("<space>", self.skip)
        self.dialogue_box.bind("<MouseWheel>", self.scroll_skip)
        self.master.bind("<Return>", self.hyper_skip)

        self.speed_button_1x.bind('<Button-1>', self.speed_1x)
        self.speed_button_2x.bind('<Button-1>', self.speed_2x)

        # Set default assets speed in miliseconds
        self.default_speed = 50
        self.speed = self.default_speed

        # Set default bool checks
        self.completed = False
        self.locked = False

        # Set default values
        self.assets = None
        self.paragraph_max = 0
        self.paragraph = 1
        self.speed_multiplier = 1


                                                                                # IMPORT ASSETS #
    def import_assets(self, assets: list=None):
        """Import used assets to the class."""
        # Set values to arguments
        self.assets = assets
        self.speed = self.default_speed

        if assets == None:
            self.paragraph_counter.place_forget()
            self.dialogue_box['text']=''
        else:
            # Reset index values
            self.char_index = 0
            self.assets_index = 0
            self.assets_max = len(assets) - 1

            self.paragraph = 1
            self.paragraph_max = 0
            for item in assets:
                if isinstance(item, str):
                    self.paragraph_max += 1
                else:
                    pass
            self.paragraph_counter.place(anchor='se', relx=0.5, rely=0.95, x=400, y=-200)
            self.paragraph_counter['text'] = f'{self.paragraph}/{self.paragraph_max}'


                                                                                # IMPORT SPEED #
    def speed_1x(self, event):
        self.speed_multiplier = 1
        for button in self.speed_buttons:
            if button == event.widget:
                button['bg'] = '#654321'
            else:
                button['bg'] = '#2e2e2e'

    def speed_2x(self, event):
        self.speed_multiplier = 2
        for button in self.speed_buttons:
            if button == event.widget:
                button['bg'] = '#654321'
            else:
                button['bg'] = '#2e2e2e'


                                                                                # SKIP #
    def skip(self, event=None):
        """Skip assets or activate function."""
        print('click')
        # Nothing if assets doesn't exist
        if self.assets == None or self.locked or self.assets_index > self.assets_max:
            pass
        # Skip printing if not completed
        elif self.printing != None:
            root.after_cancel(self.printing)
            self.printing = None
            self.dialogue_box['text'] = self.assets[self.assets_index]
            self.assets_index += 1
            self.char_index = 0
        # If next item is a string, print it
        elif isinstance(self.assets[self.assets_index], str):
            self.paragraph += 1
            self.paragraph_counter['text'] = f'{self.paragraph}/{self.paragraph_max}'
            self.dialogue_box['text'] = ''
            self.print()
        # If item is a function, run it
        elif hasattr(self.assets[self.assets_index], "__call__"):
            self.assets[self.assets_index]()
            self.assets_index += 1
            _dialogue.skip()
        # If item is a integer, change speed
        elif isinstance(self.assets[self.assets_index], int):
            self.speed = self.assets[self.assets_index]
            self.assets_index += 1
            _dialogue.skip()
        # Otherwise, skip it
        else:
            print('You broke it...')
            self.assets_index += 1

    def scroll_skip(self, event=None):
        if self.assets == None or self.locked or self.assets_index > self.assets_max:
            pass
        elif self.printing != None:
            root.after_cancel(self.printing)
            self.printing = None
            self.dialogue_box['text'] = self.assets[self.assets_index]
            self.assets_index += 1
        # If next item is a string, print it
        elif isinstance(self.assets[self.assets_index], str):
            self.paragraph += 1
            self.paragraph_counter['text'] = f'{self.paragraph}/{self.paragraph_max}'
            self.dialogue_box['text'] = self.assets[self.assets_index]
            self.assets_index += 1
        # If item is a function, run it
        elif hasattr(self.assets[self.assets_index], "__call__"):
            self.assets[self.assets_index]()
            self.assets_index += 1
        # If item is a integer, change speed
        elif isinstance(self.assets[self.assets_index], int):
            self.speed = self.assets[self.assets_index]
            self.assets_index += 1
            _dialogue.scroll_skip()
        # Otherwise, skip it
        else:
            print('You broke it...')
            self.assets_index += 1

    def hyper_skip(self, event=None):
        for asset in self.assets:
            if self.assets == None or self.locked or self.assets_index > self.assets_max:
                break
            elif self.printing != None:
                root.after_cancel(self.printing)
                self.printing = None
                self.dialogue_box['text'] = self.assets[self.assets_index]
                self.assets_index += 1
            # If next item is a string, print it
            elif isinstance(self.assets[self.assets_index], str):
                self.paragraph += 1
                self.paragraph_counter['text'] = f'{self.paragraph}/{self.paragraph_max}'
                self.dialogue_box['text'] = self.assets[self.assets_index]
                self.assets_index += 1
            # If item is a function, run it
            elif hasattr(self.assets[self.assets_index], "__call__"):
                self.assets[self.assets_index]()
                self.assets_index += 1
            # If item is a integer, change speed
            elif isinstance(self.assets[self.assets_index], int):
                self.speed = self.assets[self.assets_index]
                self.assets_index += 1
            # Otherwise, skip it
            else:
                print('You broke it...')
                self.assets_index += 1



                                                                                # PRINT #
    def print(self):
        """Print assets letter by letter according based on speed."""
        # Create easier to use variables
        _assets = self.assets
        _assets_index = self.assets_index
        _char_index = self.char_index
        _speed = round(self.speed/self.speed_multiplier)

        # Find max characters to print
        _char_max = len(_assets[_assets_index]) - 1

        # Set completed to False
        self.completed = False

        # If printing not completed and not skipped
        if _char_index < _char_max and _char_index != -1:
            # Add current assets character and set next character
            self.dialogue_box['text'] += _assets[_assets_index][_char_index]
            self.char_index += 1

            # Continue printing
            self.printing = self.master.after(_speed, self.print)

        # If printing completed
        else:
            # Reset character index
            self.char_index = 0

            # Set next assets
            self.assets_index += 1

            #Set completed to True
            self.completed = True
            self.printing = None


# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Dialogue Prototype")
    root.geometry("1024x576")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#1e1e1e'

    # Import Dialogue
    _dialogue = Dialogue(root)

    _test_label = tkin.Label(_dialogue.master,
                             bg='#1e1e1e', fg="#f1f1f1",
                             text="I am here!",
                             font=("System", 30))


    def label_create():
        _test_label.place(anchor='center', relx=0.5, rely=0.3)


    def label_destroy():
        _test_label.destroy()

    def _unlock():
        """Unlock dialogue and destroy button."""
        _dialogue.locked = False
        _unlock_button.destroy()

    def _lock():
        _dialogue.locked = True

    _unlock_button = tkin.Button(_dialogue.master,
                                 text="Click to unlock",
                                 bg='#654321', fg="#f1f1f1",
                                 activebackground="#644321",
                                 activeforeground="#e1e1e1",
                                 font=("System", 18),
                                 command=_unlock)

    def button_create():
        _unlock_button.place(anchor='center', relx=0.5, rely=0.5)
        _lock()


    _assets = ["This is a test!",
               "Is this working?",
               100, 'I made it a little too slow...',
               10, 'WOAH WOAH WOAH. TOO FAST!',
               50, "I think I've calmed down now.",
               "Try clicking me to create a label!",
               label_create,
               "Wow. It did work...",
               "Maybe click me to destroy it?",
               label_destroy,
               "And there it goes!",
               "Now let's test if unlocking works!",
               "Try to click me!",
               button_create,
               "Only worked after you unlocked it, right?",
               "AND THAT'A A WRAP!",
               "Call it a flex?",
               _dialogue.import_assets]


    _dialogue.import_assets(_assets)
    # Start printing
    _dialogue.print()

                                                                                # INITIALIZE ROOT #
    root.mainloop()
