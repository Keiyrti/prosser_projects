import tkinter as tkin
import assets

if __name__ == '__main__':
    root = tkin.Tk()
    root.geometry("1024x576")
    root.minsize(1024, 576)

    program = assets.MainWindow(root)

    PLAYER = assets.Player()

    def title_screen():
        program.title = tkin.Label(program.main_frame,
                                bg="#1e1e1e",
                                fg="#f1f1f1",
                                text="T I M E L I N E",
                                font=("System", 128))
        program.title.place(anchor="center", relx=0.5, rely=0.2)

        program.start_options = tkin.Frame(program.main_frame,
                                        bg="#2e2e2e")
        program.start_options.place(anchor="center", relx=0.5, rely=0.6,
                                 relwidth=0.3, relheight=0.5)

        program.start_options.grid_rowconfigure([0, 1, 2], weight=1)
        program.start_options.grid_columnconfigure(0, weight=1)

        program.start_button = tkin.Button(program.start_options,
                                        bg="#654321",
                                        fg="#f1f1f1",
                                        text='Start Game',
                                        font=('System', 18))
        program.start_button.grid(row=0, column=0, sticky='nsew',
                               padx=30, pady=20)

        program.options_button = tkin.Button(program.start_options,
                                          bg="#654321",
                                          fg="#f1f1f1",
                                          text='Options',
                                          font=('System', 18))
        program.options_button.grid(row=1, column=0, sticky='nsew',
                                 padx=30, pady=20)

        program.exit_button = tkin.Button(program.start_options,
                                       bg="#654321",
                                       fg="#f1f1f1",
                                       text='Exit',
                                       font=('System', 18),
                                       command=program.master.destroy)
        program.exit_button.grid(row=2, column=0, sticky='nsew',
                              padx=30, pady=20)


    def start_screen():
        program.start_options.destroy()
        program.title.destroy()

        dialog = assets.Dialogue(program.master)

        def player_name():
            _text: list = ["So... this is a long way you have traveled, child.",
                           "What is your name?"]
            dialog.import_assets(_text, get_name)

        def get_name():
            _name: str
            def _unlock(event):
                _name = _input.get()
                dialog.locked = False
                _text = [f"Hello then, {_name}..."]
                dialog.import_assets(_text, end_message)
                _input.destroy()

            _input = assets.player_input(program.main_frame, _unlock)
            dialog.locked = True

        def end_message():
            _text = ['I wish you luck then, young one...\nBe safe on your Journey.', 'It is a dangerous land.']
            dialog.import_assets(_text, enter_world)

        def enter_world():
            dialog.dialog_box['text'] = ''
            program.initizalize_menu()

        player_name()
        dialog.print()

    title_screen()
    program.start_button['command'] = start_screen


    root.mainloop()
