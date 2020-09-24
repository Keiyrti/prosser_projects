"""Module to track PLAYER's input."""

import tkinter as tkin

class player_input(tkin.Entry):
    def __init__(self, master, func=None, cnf={}, **kw):
        tkin.Entry.__init__(self, master, cnf)
        self['bg']='#2e2e2e'
        self['fg']='#f1f1f1'
        self['font']=("System", 18)
        self['justify']='center'

        self.place(anchor='center', relx=0.5, rely=0.5, relheight=0.1, relwidth=0.6)

        self.bind("<Return>", func)
