"""A Menu Button Prototype."""

import tkinter as tkin

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

        self.menu_frame = tkin.Frame(master, bg="#2e2e2e")

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
    root.mainloop()
