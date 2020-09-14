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

        # Create dialogue frame
        self.dialogue_frame = tkin.Frame(master,
                                         bg="#654321")
        self.dialogue_frame.place(anchor='s', relx=0.5, rely=0.95,
                                  width=800, height=200)

        # Set grid properties
        self.dialogue_frame.grid_rowconfigure(0, weight=1)
        self.dialogue_frame.grid_columnconfigure(0, weight=1)

        # Create dialogue box
        self.dialogue_box = tkin.Label(self.dialogue_frame,
                                     bg="#2e2e2e", fg="#f1f1f1",
                                     font="System")
        self.dialogue_box.grid(row=0, column=0, sticky="nsew",
                             padx=10, pady=10)

        # Bind LMB and SPACE to skipping dialogue
        self.dialogue_box.bind("<Button-1>", self.skip)
        self.master.bind("<space>", self.skip)

        # Set default assets speed in miliseconds
        self.default_speed = 50
        self.speed = self.default_speed

        # Set default bool checks
        self.completed = False
        self.locked = False

        # Set default values
        self.assets = None


                                                                                # IMPORT ASSETS #
    def import_assets(self, assets: list=None):
        """Import used assets to the class."""
        # Set values to arguments
        self.assets = assets
        self.speed = self.default_speed

        # Reset index values
        self.char_index = 0
        self.assets_index = 0
        self.assets_max = len(assets) - 1


                                                                                # IMPORT SPEED #
    def import_speed(self, speed):
        """Change assets speed based in milliseconds."""
        # Set values to arguments
        self.speed = speed


                                                                                # SKIP #
    def skip(self, event=None):
        """Skip assets or activate function."""
        # Nothing if assets doesn't exist
        if self.assets == None:
            pass
        # Nothing if dialogue box is locked
        elif self.locked:
            pass
        # Nothing if assets is finished
        elif self.assets_index > self.assets_max:
            pass
        # Skip printing if not completed
        elif self.completed == False:
            self.char_index = -1
        # If next item is a string, print it
        elif isinstance(self.assets[self.assets_index], str):
            self.dialogue_box['text'] = ''
            self.print()
        # Otherwise, run it
        else:
            self.assets[self.assets_index]()
            self.assets_index += 1


                                                                                # PRINT #
    def print(self):
        """Print assets letter by letter according based on speed."""
        # Create easier to use variables
        _assets = self.assets
        _assets_index = self.assets_index
        _char_index = self.char_index

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
            self.dialogue_frame.after(self.speed, self.print)

        # If printing completed or skipped
        else:
            # Set assets to assets
            self.dialogue_box['text'] = _assets[_assets_index]

            # Reset character index
            self.char_index = 0

            # Set next assets
            self.assets_index += 1

            #Set completed to True
            self.completed = True


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
        root.after(0, _dialogue.skip)


    def label_destroy():
        _test_label.destroy()
        root.after(0, _dialogue.skip)

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
        root.after(0, _dialogue.skip)
        root.after(0, _lock)


    _assets = ["This is a test!",
               "Is this working?",
               "Try clicking me to create a label!",
               label_create,
               "Wow. It did work...",
               "Maybe click me to destroy it?",
               label_destroy,
               "And there it goes!",
               "Now let's test if unlocking works!",
               button_create,
               "Try to click me!",
               "Only worked after you unlocked it, right?",
               "AND THAT'A A WRAP!",
               "Call it a flex?"]


    _dialogue.import_assets(_assets)
    # Start printing
    _dialogue.print()

                                                                                # INITIALIZE ROOT #
    root.mainloop()
