"""A Menu Button Prototype."""

import tkinter as tkin
                                                                                # Define the Main Window class
class MainWindow:
    """Class for easily importing a menu system."""

                                                                                # INITIALIZATION SETTINGS #
    def __init__(self, master):
        """Set default parameters on initialization."""
        # Set master
        self.master = master

        # Set grid properties
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)

        # Create main frame
        self.main_frame = tkin.Frame(master, bg="#1e1e1e")
        self.main_frame.grid(row=0, column=0, sticky='nsew')

        # Create an invisible picture for later use
        self._invis_pic = tkin.PhotoImage(width=1, height=1)


                                                                                # INITIALIZE MENU #
    def initialize_menu(self, title=''):
        """Create menu system."""
        # Bind TAB to opening menu
        self.master.bind("<Tab>", self.toggle_menu)

        # Define health and width of menu
        self.menu_width: float = 0.25
        self.menu_height: float = 1

        # Create menu frame
        self.menu_frame = tkin.Frame(self.master, bg="#2a2a2a")
        self.menu_frame.lift()

        # Set grid properties
        self.menu_frame.grid_rowconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)

        # Create close button
        self.close_button = tkin.Button(self.menu_frame,
                                   bg='#ff6961',
                                   fg='#f1f1f1',
                                   image=self._invis_pic,
                                   width=32, height=32,
                                   text=u'\u2715',
                                   font=('System', 20),
                                   compound='c',
                                   command=self.master.destroy)
        self.close_button.place(anchor='nw', relx=0.8, rely=0.91)

        # Create Title of menu
        self.menu_title = tkin.Label(self.menu_frame,
                                      bg=self.menu_frame['bg'],
                                      fg="#f1f1f1",
                                      text=title,
                                      font=('System', 20))
        self.menu_title.grid(sticky='new', pady=30)

        # Define bool for menu opened
        self._menu_opened = False


                                                                                # TOGGLE MENU #
    def toggle_menu(self, event):
        """Toggle menu displayed."""
        # Toggle menu opened bool
        self._menu_opened = not self._menu_opened

        # Open menu
        if self._menu_opened:
            self.menu_frame.place(relwidth=self.menu_width,
                                  relheight=self.menu_height)

        # Close menu
        else:
            self.menu_frame.place_forget()

# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Menu Prototype")
    root.geometry("1024x576")
    root.minsize(1024, 576)

    # Import Main Window
    program = MainWindow(root)

    # Initilize menu for testing
    program.initialize_menu('Test Name')

                                                                                # INITIALIZE ROOT #
    root.mainloop()
