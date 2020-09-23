"""An Improved Dialogue System by Kirati Kiviniemi."""

import tkinter as tkin
import sys

sys.setrecursionlimit(1500)


class Dialogue:
  """Class for easily importing and printing strings."""

  # Appearance variables
  main_color = "#654321"
  secondary_color = "#2e2e2e"
  text_color = "#f1f1f1"
  font = ("Sawasdee", 12)
  widget_font = ("System", 8)

  def __init__(self, master):
    """Set default parameters on initialization."""
    # Set master
    self.master = master

    self._invis_pic = tkin.PhotoImage(width=1, height=1)

    # Create dialogue frame
    self.bg_frame = tkin.Frame(
        master,
        bg=self.main_color,
        cursor="hand2")
    self.bg_frame.place(
        anchor='s', relx=0.5, rely=0.95,
        width=800, height=200)

    # Create dialogue box
    self.text_box = tkin.Label(
        self.bg_frame,
        bg=self.secondary_color, fg=self.text_color,
        font=self.font,
        wraplength=750,
        cursor="hand2")
    self.text_box.place(
        anchor='center',
        relx=0.5, rely=0.5,
        width=780, height=180)

    # Create paragraph counter widget
    self.text_counter = tkin.Label(
        self.master,
        bg=self.main_color , fg=self.text_color,
        image=self._invis_pic,
        compound='c',
        width=60, height=10,
        justify='right')

    # Create speed 1x widget
    self.speed_1x = tkin.Label(
        self.master,
        bg=self.main_color, fg=self.text_color,
        image=self._invis_pic,
        compound='c',
        width=30, height=10,
        text='1x',
        justify='center',
        cursor="hand2",
        font=self.widget_font)
    self.speed_1x.place(
        anchor='sw',
        relx=0.5, rely=0.95,
        x=-400, y=-200)

    # Create speed 2x widget
    self.speed_2x = tkin.Label(
        self.master,
        bg=self.secondary_color, fg=self.text_color,
        image=self._invis_pic,
        compound='c',
        width=30, height=10,
        text='2x',
        justify='center',
        cursor="hand2",
        font=self.widget_font)
    self.speed_2x.place(
        anchor='sw',
        relx=0.5, rely=0.95,
        x=-370, y=-200)

    # Define list of buttons
    self.speed_x: list = [self.speed_1x, self.speed_2x]

    # Definte default locked value
    self.locked = False

    # Bind events
    self.text_box.bind('<Button-1>', self.click_event)
    self.text_box.bind('<Button-3>', self.reverse_click_event)
    self.master.bind('<Return>', self.hyper_action)


  # Represent Method
  def __repr__(self):
    return "Dialogue Box Object"


  # Set Attribute Method
  def __setattr__(self, name, value):
    """Check the set attribute."""
    object.__setattr__(self, name, value)
    if name == 'items':
      if value != None:
        self.items_index = 0
        self.items_next = 1
        self.items_prev = -1
        self.char_index = 0
        self.char_max = 0
        self.items_max = len(value) - 1
        self.speed = 50
        self.items_completed = False
        self.bind = False
        self.skip = False
        self.printing = None
        self.hyper = False
        self.action()
      else:
        self.items = []
    elif name == 'text':
        self.text_box['text'] = value
    else:
        pass


  # Update Method
  def update(self, **kw):
    """Update item index and execute action."""
    self.items_index += 1
    self.items_max = len(self.items) - 1
    self.items_next = self.items_index + 1
    self.items_prev = self.items_index - 1
    self.char_index = 0

    self.items_completed = False

    if self.hyper == True:
      self.hyper_action()
    else:
      self.action()


  # Click Method
  def click_event(self, event=None):
    """Skip or perform action when skipped."""
    if self.items == [] or self.locked == True or self.items_next > self.items_max:
      pass
    elif self.items_completed == False:
      self.skip = True
      if self.printing != None:
        self.master.after_cancel(self.printing)
        self.printing = None

    self.action()

  def reverse_click_event(self, event=None):
    """Skip or perform action."""
    if self.items == [] or self.locked == True:
      pass
    elif self.items_index == 0:
      _item = self.items[self.items_index]
      self.text = _item
    elif self.items_completed == False:
      self.skip = True
      if self.printing != None:
        self.master.after_cancel(self.printing)
        self.printing = None

    self.backwards()


  # Action Method
  def action(self, event=None):
    """Do logic."""
    if self.items == [] or self.locked == True or self.items_next > self.items_max:
      pass
    elif self.items_completed == True:
      self.update()
    else:
      _item = self.items[self.items_index]
      if isinstance(_item, str):
        self.char_max = len(_item)
        if self.bind != False or self.skip == True:
          self.bind = False
        else:
          self.text = ''

        self.print()
      elif hasattr(_item, "__call__"):
        _item()
        del self.items[self.items_index]
        self.items_index -= 1
        self.update()
      elif isinstance(_item, float):
        _pause = round(_item)
        del self.items[self.items_index]
        self.items_index -= 1
        if self.skip == True:
          self.update()
        else:
          self.printing = self.master.after(_pause, self.update)
      elif isinstance(_item, int):
        self.speed = _item
        del self.items[self.items_index]
        self.items_index -= 1
        self.update()

      self.skip = False


  def backwards(self, event=None):
    print(self.items)
    if self.items == [] or self.locked == True:
      pass
    elif self.items_index == 0:
      _item = self.items[self.items_index]
      self.text = _item
    else:
      _item = self.items[self.items_prev]
      self.text = _item
      self.items_index -= 1
      self.items_prev = self.items_index - 1
      self.items_next = self.items_index + 1




  # HYPER ACTION METHOD
  def hyper_action(self, event=None):
    """Instant skip."""
    self.hyper = True
    self.skip = True

    if self.printing != None:
      # If printing, stop
      self.master.after_cancel(self.printing)
      self.printing = None
    if (self.items == []
        or self.locked == True
        or self.items_next > self.items_max):
      # If cannot continue, end hyper and skip
      self.hyper = False
      self.skip = False
    elif self.items_completed == True:
      # If item is complete, update item
      self.update()
    else:
      # If item isn't complete, perform item
      _item = self.items[self.items_index]

      if isinstance(_item, str):
        self.char_max = len(_item)
        if self.bind == True:
          self.bind = False
        else:
          self.text_box['text'] = ''

        self.print()
      elif hasattr(_item, "__call__"):
        _item()
        del self.items[self.items_index]
        self.items_index -= 1
        self.update()
      elif isinstance(_item, float):
        self.update()
        del self.items[self.items_index]
        self.items_index -= 1
      elif isinstance(_item, int):
        self.speed = _item
        del self.items[self.items_index]
        self.items_index -= 1
        self.update()


  # Print Method
  def print(self):
    _speed = self.speed
    if self.char_index >= self.char_max:
      self.printing = None
      self.items_completed = True
      if self.hyper == True:
        self.update()
    elif self.items[self.items_index][self.char_index] == '+':
      self.bind = True
      self.update()
    else:
      self.text_box['text'] += self.items[self.items_index][self.char_index]
      self.char_index += 1
      if self.skip == True:
        self.print()
      else:
        self.printing = self.master.after(_speed, self.print)



if __name__ == '__main__':

  # Root creation
  root = tkin.Tk()
  root.title("Dialogue Prototype")
  root.geometry("1024x576")
  root.minsize(1024, 576)

  # Set root properties
  root['bg'] = '#d1d1d1'
  root.text = "#1e1e1e"

  # Import Dialogue
  _dialogue = Dialogue(root)


  def _lock():
    def _unlock():
      _dialogue.locked = False
      _unlockbutton.destroy()
      _dialogue.action()

    _unlockbutton = tkin.Button(
        root,
        text="unlock",
        command=_unlock)
    _unlockbutton.place(
        anchor = 'center',
        relx=0.5, rely=0.5)

    _dialogue.locked = True


  _items = [
      "This is a test!",
      "Is this working?",
      "What happens when I tweak the speed a bit?",
      100, 'It seems that I made it a little too slow...',
      10, 'WOAH WOAH WOAH. TOO FAST!',
      50, "I think it's calmed down now.",
      "How about large chunks of text?",
      50, "Try clicking around here to create a label!",
      "Wow. It worked...",
      "Maybe click again to destroy it?",
      "And there it goes!",
      "Now let's test if unlocking works!",
      "Try to click here!",
      _lock,
      "Only worked after you unlocked it, right?",
      "AND THAT'S A WRAP!",
      "Call it a flex.",
      'null']

  _dialogue.items = _items

  root.mainloop()
