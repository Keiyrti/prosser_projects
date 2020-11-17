import tkinter as tk
from tkinter import font

class BlockRoot(tk.Tk):
  def __init__(self, master=None):
    '''Call init of super and create default values.'''
    super().__init__(master)
    self.wm_overrideredirect(True)
    self.geometry("320x180+200+200")

    self.colors_background = "#2C2F33"
    self.colors_titlebar = "#23272A"

    self.title_font = font.Font(family="Roboto Mono", size=12, weight='normal')

    self.invis_pic = tk.PhotoImage(width=1, height=1)

    self.name = "Default Window"

  def mainloop(self):
    '''Create and place default widgets on mainloop.'''
    self.titlebar = tk.Frame(
      self,
      bg=self.colors_titlebar,
      height=30)
    self.titlebar_title = tk.Label(
      self.titlebar,
      bg=self.colors_titlebar, fg='#ffffff',
      text=self.name,
      font=self.title_font)
    self.close_button = tk.Button(
      self.titlebar,
      bg=self.colors_titlebar, fg='#ffffff',
      activebackground='#E65653', activeforeground="#ffffff",
      bd=0, cursor="hand2",
      text="⨉",
      font=self.title_font,
      command=self.destroy)

    self.contents = tk.Canvas(
      self,
      bg=self.colors_background,
      bd=0, highlightthickness=0)

    self.titlebar.pack(expand=1, fill="x")
    self.titlebar_title.place(
      anchor='center',
      relx=0.5, rely=0.5)
    self.close_button.place(
      anchor='e',
      relx=1, rely=0.5)

    self.contents.pack(expand=1, fill='both')

    def close_button_highlight(event):
      if event.widget['bg'] == "#FF605C":
        event.widget['bg'] = self.colors_titlebar
      else:
        event.widget['bg'] = "#FF605C"

    self.close_button.bind("<Enter>", close_button_highlight)
    self.close_button.bind("<Leave>", close_button_highlight)

    def get_pos(event):
      xwin = self.winfo_x()
      ywin = self.winfo_y()
      startx = event.x_root
      starty = event.y_root

      ywin = ywin - starty
      xwin = xwin - startx


      def move_window(event):
        self.geometry('+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
      startx = event.x_root
      starty = event.y_root


      self.titlebar.bind('<B1-Motion>', move_window)
      self.titlebar_title.bind('<B1-Motion>', move_window)
    self.titlebar.bind('<Button-1>', get_pos)
    self.titlebar_title.bind('<Button-1>', get_pos)

    super().mainloop()


  def move_window(event):
    pass


if __name__ == "__main__":
  root = BlockRoot()
  root.mainloop()