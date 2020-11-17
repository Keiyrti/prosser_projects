import tkinter as tk
import os
from tkinter import font

class Dialogue(tk.Frame):
  '''Textbox for displaying dialogue.'''

  def __init__(self, master):
    '''Call super init and create default values for textbox.'''
    super().__init__(master)
    self.master = master

    self['width'] = 1120
    self['height'] = 200
    self['bg'] = '#e1e1e1'

    self.font = font.Font(family='pixelmix', size=12, weight='normal')

    self.text_box = tk.Label(
      self,
      bg=self['bg'],
      justify='center', font=self.font)
    self.text_box.place(
      anchor='center',
      relx=0.5, rely=0.5)

    self.text_box.bind("<Button-1>", self.click)
    self.bind("<Button-1>", self.click)

    self.printing = None
    self.speed: int = 50
    self.concat = False
    self.skip = False

  def start(self, assets: list):
    '''Start system and import assets.'''
    self.items: list = assets
    self.item_num_max: int = len(assets) - 1
    self.item_num: int = 0
    self.item = self.switch(self.item_num)
    self.concat = False
    self.skip = False

    self.speed: int = 50

  def click(self, event):
    '''Handle click event for skipping and continuing.'''
    self.item_num_max: int = len(self.items) - 1

    if self.text_box['state'] == 'disabled' or self.item_num == self.item_num_max:
      pass
    # TODO: Fix skip system!!!
    elif self.printing != None:
      self.skip = True
    else:
      self.item_num += 1
      self.switch(self.item_num)

  def switch(self, item_num: int):
    '''Switch list items.'''
    self.item = self.items[item_num]

    if self.printing != None:
      self.after_cancel(self.printing)

    if isinstance(self.item, str):
      if self.concat != False:
        self.item_parts = list(self.item)
        self.items[item_num-1] = self.items[item_num-1][:-1]
        self.items[item_num-1] += self.item

        del self.items[item_num]
        self.item_num -= 1

        self.concat = False
      else:
        self.text_box['text'] = ''
        self.item_parts = list(self.item)
    else:
      del self.items[item_num]
      self.item_num -= 1

    self.action()

  def action(self):
    '''Activate list item depending on object type.'''
    if isinstance(self.item, str):
      self.print()
    if isinstance(self.item, int):
      self.speed = self.item
      self.click(None)
    if isinstance(self.item, float):
      delay = round(self.item)
      self.after(delay, lambda: self.click(None))
    if callable(self.item):
      self.item()
    else:
      pass

  def print(self):
    '''Print string item types.'''
    if len(self.item_parts) > 0:
      char = self.item_parts.pop(0)

      if self.skip == True:
        speed = 0
      else:
        speed = self.speed

      if len(self.item_parts) == 0 and char == '&':
        self.concat = True
        self.click(None)
      else:
        self.text_box['text'] += char
        self.printing = self.after(speed, self.print)
    else:
      pass


class Dialogue_Window(tk.Tk):
  '''Default environment for Dialogue system testing and displaying.'''
  def __init__(self):
    '''Call super init and create default objects.'''
    super().__init__(None)
    self.title("Dialogue System")
    self['bg'] = '#2e2e2e'

    dir_path = os.path.dirname(os.path.realpath(__file__))
    self.iconphoto(False, tk.PhotoImage(file=dir_path+"\\assets\\icon.png"))

    self.dialogue_box = Dialogue(self)
    self.dialogue_box.pack(side='bottom')


if __name__ == "__main__":
  '''Run this code only if running this file.'''
  root = Dialogue_Window()

  def test():
    print(root.dialogue_box.items)

  asset_list = [
    "Hello!\nThis is a simple test to see if the simple print system is up and running!&",
    1000.0,
    "\nPlease do not be alarmed.",
    test,
    20,
    "Test Number Two!"
    ]
  root.dialogue_box.start(asset_list)
  root.mainloop()