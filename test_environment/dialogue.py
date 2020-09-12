"""A Menu Button Prototype."""

import tkinter as tkin

class Dialogue:
    def __init__(self, master):
        self.master = master
        self.dialogue_frame = tkin.Frame(master,
                                         bg="#654321")
        self.dialogue_frame.place(anchor='s', relx=0.5, rely=0.95,
                                  width=800, height=200)
        self.dialogue_frame.grid_rowconfigure(0, weight=1)
        self.dialogue_frame.grid_columnconfigure(0, weight=1)
        self.dialog_box = tkin.Label(self.dialogue_frame,
                                     bg="#2e2e2e", fg="#f1f1f1",
                                     font="System")
        self.dialog_box.grid(row=0, column=0, sticky="nsew",
                             padx=10, pady=10)
        self.dialog_box.bind("<Button-1>", self.skip)
        self.master.bind("<space>", self.skip)

        self.default_speed = 50

        self.function = None
        self.speed = self.default_speed
        self.completed = False
        self.locked = False


    def import_assets(self, text='', func=None):
        self.text = text
        self.function = func
        self.speed = self.default_speed

        self.char_index = 0
        self.text_index = 0
        self.text_max = len(text) - 1


    def import_speed(self, speed):
        self.speed = speed


    def skip(self, event):
        if self.locked:
            pass
        elif not self.completed:
            self.char_index = -1
        elif self.text_index > self.text_max and self.function != None:
            self.function()
        elif self.text_index > self.text_max:
            pass
        else:
            self.dialog_box['text'] = ''
            self.print()


    def print(self):
        _text = self.text
        _text_index = self.text_index
        _char_index = self.char_index
        _char_max = len(_text[_text_index]) - 1
        self.completed = False

        if _char_index < _char_max and _char_index != -1:
            self.dialog_box['text'] += _text[_text_index][_char_index]
            self.char_index += 1
            self.dialogue_frame.after(self.speed, self.print)
        else:
            self.dialog_box['text'] = _text[_text_index]
            self.char_index = 0
            self.text_index += 1
            self.completed = True


class MenuWindow:
    def __init__(self, master):
        self.master = master
        master.title("Menu Prototype")
        master.bind("<Tab>", self.toggle_menu)

        self.menu_width = 0.25
        self.menu_height = 1

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.main_frame = tkin.Frame(master, bg="#1e1e1e")
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        self.menu_frame = tkin.Frame(master, bg="#2a2a2a")
        self.menu_frame.lift()

        self._menu_opened = False


    def toggle_menu(self, event):
        self._menu_opened = not self._menu_opened

        if self._menu_opened:
            self.menu_frame.place(relwidth=self.menu_width, relheight=self.menu_height)
        else:
            self.menu_frame.place_forget()

if __name__ == '__main__':
    root = tkin.Tk()
    program = MenuWindow(root)
    root.geometry("1024x576")
    root.minsize(1024, 576)

    def testFunction():
        _text = ["This is a test!", "You can add dialogue here!", "Click to create a label."]
        _dialogue.import_assets(_text, testFunction2)

    def testFunction2():
        _test_label = tkin.Label(_dialogue.master,
                                 bg='#1e1e1e', fg="#f1f1f1",
                                 text="I am here!",
                                 font=("System", 30))
        _test_label.place(anchor='center', relx=0.5, rely=0.3)
        _text = ["Now click to destroy it!"]
        _dialogue.import_assets(_text, lambda: testFunction3(_test_label))

    def testFunction3(label):
        label.destroy()
        _text = ["It's as simple as that!", '']
        _dialogue.locked = True
        def _unlock():
            _dialogue.locked = False
            _unlock_button.destroy()
        _unlock_button = tkin.Button(_dialogue.master,
                                     text="Unlock the dialogue!",
                                     command=_unlock)
        _unlock_button.place(anchor='center', relx=0.5, rely=0.5)
        _dialogue.import_assets(_text)

    _dialogue = Dialogue(program.main_frame)
    testFunction()
    _dialogue.print()

    root.mainloop()
