"""A Dialogue System Prototype."""

import tkinter as tkin

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

        # Set default text speed in miliseconds
        self.default_speed = 50
        self.speed = self.default_speed

        # Set default function
        self.function = None

        # Set default bool checks
        self.completed = False
        self.locked = False


                                                                                # IMPORT ASSETS #
    def import_assets(self, text='', func=None):
        """Import used assets to the class."""
        # Set values to arguements
        self.text = text
        self.function = func
        self.speed = self.default_speed

        # Reset index values
        self.char_index = 0
        self.text_index = 0
        self.text_max = len(text) - 1


                                                                                # IMPORT SPEED #
    def import_speed(self, speed):
        """Change text speed based in miliseconds."""
        # Set values to arguements
        self.speed = speed


                                                                                # SKIP #
    def skip(self, event=None):
        """Skip text or activate function."""
        # Nothing if dialogue box is locked
        if self.locked:
            pass

        # Skip dialogue printing if not completed
        elif not self.completed:
            self.char_index = -1

        # Activate function if added and text completed
        elif self.text_index > self.text_max and self.function != None:
            self.function()

        # Nothing if function missing and text completed
        elif self.text_index > self.text_max:
            pass

        # Continue priting if text not completed
        else:
            self.dialogue_box['text'] = ''
            self.print()


                                                                                # PRINT #
    def print(self):
        """Print text letter by letter according based on speed."""
        # Create easier to use variables
        _text = self.text
        _text_index = self.text_index
        _char_index = self.char_index

        # Find max characters to print
        _char_max = len(_text[_text_index]) - 1

        # Set completed to False
        self.completed = False

        # If printing not completed and not skipped
        if _char_index < _char_max and _char_index != -1:
            # Add current text character and set next character
            self.dialogue_box['text'] += _text[_text_index][_char_index]
            self.char_index += 1

            # Continue printing
            self.dialogue_frame.after(self.speed, self.print)

        # If printing completed or skipped
        else:
            # Set text to text
            self.dialogue_box['text'] = _text[_text_index]

            # Reset character index
            self.char_index = 0

            # Set next text
            self.text_index += 1

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

                                                                                # FIRST SECTION #
    def FirstSection():
        """Initial dialogue."""
        # Set text
        _text = ["This is a test!",
                 "You can add dialogue here!",
                 "Click to create a label."]

        # Import text and reference next section
        _dialogue.import_assets(_text, SecondSection)


                                                                                # SECOND SECTION #
    def SecondSection():
        """Second section of dialogue."""
        # Create test label
        _test_label = tkin.Label(_dialogue.master,
                                 bg='#1e1e1e', fg="#f1f1f1",
                                 text="I am here!",
                                 font=("System", 30))
        _test_label.place(anchor='center', relx=0.5, rely=0.3)

        # Set text
        _text = ["Now click to destroy it!"]

        # Import text and reference next section
        _dialogue.import_assets(_text, lambda: ThirdSection(_test_label))


                                                                                # THIRD SECTION #
    def ThirdSection(label):
        """Third section of dialogue."""
        # Destroy test label
        label.destroy()

        # Set text
        _text = ["It's as simple as that!",
                 'You can even lock dialogue.']

        # Import text and reference next section
        _dialogue.import_assets(_text, FourthSection)


                                                                                # FOURTH SECTION #
    def FourthSection():
        """Fourth section of dialogue."""
        # UNLOCK #
        def _unlock():
            """Unlock dialogue and destroy button."""
            _dialogue.locked = False
            _unlock_button.destroy()

        # Create unlocked button
        _unlock_button = tkin.Button(_dialogue.master,
                                     text="Click to unlock",
                                     bg='#654321', fg="#f1f1f1",
                                     activebackground="#644321",
                                     activeforeground="#e1e1e1",
                                     font=("System", 18),
                                     command=_unlock)
        _unlock_button.place(anchor='center', relx=0.5, rely=0.5)

        # Lock dialogue
        _dialogue.locked = True

        # Set text
        _text = ["Just like that!"]

        # Import text and end dialogue
        _dialogue.import_assets(_text)

    # Import Dialogue
    _dialogue = Dialogue(root)

    # Initalize First Section
    FirstSection()

    # Start printing
    _dialogue.print()

                                                                                # INITIALIZE ROOT #
    root.mainloop()
