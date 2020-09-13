"""Timeline by Kirati Kiviniemi."""

import tkinter as tkin
import assets


# Code for running this specific file
if __name__ == '__main__':

    # Root creation
    root = tkin.Tk()
    root.title('Timeline a0.1')
    root.geometry("1024x576")
    root.minsize(1024, 576)

    # Import Main Window
    program = assets.MainWindow(root)

    # Import Player
    PLAYER = assets.Player()


                                                                                # TITLE SCREEN
    def title_screen():
        """Create title screen for game."""
        # Create title
        program.title = tkin.Label(program.main_frame,
                                bg="#1e1e1e",
                                fg="#f1f1f1",
                                text="T I M E L I N E",
                                font=("System", 128))
        program.title.place(anchor="center", relx=0.5, rely=0.2)

        # Create start menu frame
        program.start_options = tkin.Frame(program.main_frame,
                                        bg="#2e2e2e")
        program.start_options.place(anchor="center", relx=0.5, rely=0.6,
                                 relwidth=0.3, relheight=0.5)

        # Set grid properties
        program.start_options.grid_rowconfigure([0, 1, 2], weight=1)
        program.start_options.grid_columnconfigure(0, weight=1)

        # Create start button
        program.start_button = tkin.Button(program.start_options,
                                        bg="#654321",
                                        fg="#f1f1f1",
                                        text='Start Game',
                                        font=('System', 18))
        program.start_button.grid(row=0, column=0, sticky='nsew',
                               padx=30, pady=20)

        # Create options button
        program.options_button = tkin.Button(program.start_options,
                                          bg="#654321",
                                          fg="#f1f1f1",
                                          text='Options',
                                          font=('System', 18))
        program.options_button.grid(row=1, column=0, sticky='nsew',
                                 padx=30, pady=20)

        # Create exit button
        program.exit_button = tkin.Button(program.start_options,
                                       bg="#654321",
                                       fg="#f1f1f1",
                                       text='Exit',
                                       font=('System', 18),
                                       command=program.master.destroy)
        program.exit_button.grid(row=2, column=0, sticky='nsew',
                              padx=30, pady=20)


                                                                                # START CUTSCENE #
    def start_cutscene():
        """Start of the game, player name and starting stats."""
        # Destroy old assets
        program.start_options.destroy()
        program.title.destroy()

        # Import Dialogue
        dialogue = assets.Dialogue(program.master)


        # BEGINNING DIALOGUE#
        def beginning_dialogue():
            """Opening scene dialogue."""
            # Set text
            _text: list = ["It's warm, cozy even.\n"
                           + "You can feel the heat radiating from a nearby fireplace.\n"
                           + "As you feel slightly more awake, you notice light tapping on the roof of this unknown dwelling.\n"
                           + "The rain almost inviting you to sleep once more.",

                           '"Ah, finallly awake I see."',

                           'You jump, hearing an unknown voice.\n'
                           + 'Turning your head in its direction, you notice an old man.\n'
                           + 'He simply continues speaking, choosing to ignore your confusion.',

                           '"So... this is a long way you have traveled, child."\n'
                           + '"You may have been dead by now, had I not brought you here."',

                           'Taking note of you silence, he asks a simple question...',

                           '"What is your name, young one?"']

            # Import text and reference next section
            dialogue.import_assets(_text, player_name)


        # PLAYER NAME #
        def player_name():
            """Get the player's name as an input."""
            # Set name
            _name: str


            # UNLOCK #
            def _unlock(event):
                """Unlock dialogue."""
                # Set name
                _name = _input.get()
                PLAYER['name'] = _name

                # Destory _input widget
                _input.destroy()

                # Unlock dialogue
                dialogue.locked = False

                # Set text
                _text = [f'"{PLAYER["name"]}..." you answer,\n'
                         + 'ready to bolt if he becomes any more suspicious.',

                         f"Then I welcome you, {PLAYER['name']}...\n"
                         + "I do not know how you ended up in such a place,\n"
                         + "but I wish to help regardless.",

                         "Let an old man work his magic..."]

                # Import text and reference next section
                dialogue.import_assets(_text, player_stats)
                dialogue.skip()

            # Lock dialogue
            dialogue.locked = True

            # Import player input and attach unlock function
            _input = assets.player_input(program.main_frame, _unlock)


                                                                                # PLAYER STATS #
        def player_stats():
            """Get the player's starting stats."""
            # UNLOCK #
            def _unlock():
                """Unlock dialogue."""
                # Unlock dialogue
                dialogue.locked = False

                # Set text
                _text = ['I wish you luck then, young one...\n'
                         + 'Be safe on your Journey.',

                         'It is a dangerous land.']

                # Import text and reference next section
                dialogue.import_assets(_text, enter_world)
                dialogue.skip()


            # STAT SELECTOR #
            def stat_selecter():
                """Allow player to allocate skill points."""
                # Create stat frame
                _stat_frame = tkin.Frame(program.main_frame,
                                         bg='#2e2e2e')
                _stat_frame.place(anchor='center',
                                  relx=0.5, rely=0.5,
                                  relheight=0.5, relwidth=0.3)

            # Lock Dialogue
            dialogue.locked = True

            # Initialize stat selector
            _stat_selector = stat_selecter()


        # ENTER WORLD #
        def enter_world():
            """End dialogue and initialize menu."""
            # Import null
            dialogue.import_assets()
            dialogue.skip()

            # Initialize menu
            program.initialize_menu(PLAYER['name'])

        # Initialize beginning dialogue
        beginning_dialogue()

        # Start printing
        dialogue.print()

                                                                                # INITIALIZE TITLE SCREEN #
    title_screen()

    # Set command of start button
    program.start_button['command'] = start_cutscene

                                                                                # INITIALIZE ROOT #
    root.mainloop()
