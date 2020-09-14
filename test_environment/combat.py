"""Combat system."""

import tkinter as tkin
import dialogue2

                                                                                # Define the Combat Window class
class CombatWindow():
    """Class for easily implementing turnbased combat."""

                                                                                # INITIALIZE SETTINGS #
    def __init__(self, master):
        """Create Combat Window."""
        # Set master
        self.master = master

        # Create combat frame
        self.combat_frame = tkin.Frame(master,
                                       bg="#2e2e2e",
                                       width=1000,
                                       height=400)

        self.combat_frame.place(anchor="n",
                                relx=0.5, y=20)

        # Create options frame
        self.options_frame = tkin.Frame(self.combat_frame,
                                       bg="#553311")
        self.options_frame.place(width=225, height=400)

        # Create player frame
        self.player_frame = tkin.Frame(self.combat_frame,
                                       bg="#0e0e0e")
        self.player_frame.place(x=225,
                                width=225, height=400)

        # Create middle frame
        self.middle_frame = tkin.Frame(self.combat_frame,
                                       bg="#2e2e2e")
        self.middle_frame.place(x=450,
                                width=100, height=400)

        # Create enemy frame
        self.enemy_frame = tkin.Frame(self.combat_frame,
                                       bg="#0e0e0e")
        self.enemy_frame.place(x=550,
                               width=450, height=400)

# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title("Combat Prototype")
    root.geometry("1024x576")
    root.minsize(1024, 576)

    # Set root properties
    root['bg'] = '#1e1e1e'

    # Import CombatWindow
    _combat = CombatWindow(root)
    _dialogue = dialogue2.Dialogue(root)

                                                                                # INITIALIZE ROOT #
    root.mainloop()
