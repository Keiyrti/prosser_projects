"""A Menu Button Prototype."""

import tkinter as tkin

class MainWindow:
    def __init__(self, master):
        self.master = master
        master.title("Timeline v1.0")

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        self.main_frame = tkin.Frame(master, bg="#1e1e1e")
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        self._invis_pic = tkin.PhotoImage(width=1, height=1)

    def initizalize_menu(self):
        self.master.bind("<Tab>", self.open_menu)

        self.menu_width = 0.25
        self.menu_height = 1

        self.menu_frame = tkin.Frame(self.master, bg="#2a2a2a")
        self.menu_frame.lift()

        self.menu_frame.grid_rowconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)

        self.close_button = tkin.Button(self.menu_frame,
                                   bg='#ff6961',
                                   fg='#f1f1f1',
                                   image=self._invis_pic,
                                   width=32, height=32,
                                   text=u'\u2715',
                                   font=('System', 20),
                                   compound='c',
                                   command=self.master.destroy)
        self.close_button.grid(sticky='se', padx=10, pady=10)

        self._menu_opened = False

    def open_menu(self, event):
        self._menu_opened = not self._menu_opened

        if self._menu_opened:
            self.menu_frame.place(relwidth=self.menu_width, relheight=self.menu_height)
        else:
            self.menu_frame.place_forget()

if __name__ == '__main__':
    root = tkin.Tk()
    program = MainWindow(root)
    root.geometry("1024x576")
    root.minsize(1024, 576)

    program.initizalize_menu()

    root.mainloop()
