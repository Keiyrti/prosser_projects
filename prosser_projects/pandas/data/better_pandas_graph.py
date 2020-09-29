import pandas as pd
import numpy as np

import matplotlib as mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import tkinter as tkin
from tkinter import filedialog

_test_values = [0, 1, 2, 3]




class MainWindow():
  '''Main root window for graph.'''

  tabs = {}
  file = None


  class Window(FigureCanvasTkAgg):
    '''Blank canvas placeholder class.'''
    def __init__(self, master):

      self.fig = Figure(figsize=[5, 4], dpi=100)
      self.fig.add_subplot(111).plot()
      FigureCanvasTkAgg.__init__(self, figure=self.fig, master=master)
      self.get_tk_widget().place(
          anchor='center',
          relx=0.5, rely=0.5,
          relwidth=0.8, relheight=0.8)


  def __init__(self):
    self.root = tkin.Tk()
    self.root.geometry('800x600')
    self.root.minsize(800, 600)

    self.root['bg'] = '#1e1e1e'

    self.pic = tkin.PhotoImage(width=1, height=1)

    self.button_new = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=40, height=15,
        text='+',
        command=self.new_window)

    self.new_window()
    self.root.bind('<BackSpace>', self.remove_window)

    _standard = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=40, height=15,
        text='Graph',
        command=self.standard)
    _standard.place(y=30)

    _bar = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=40, height=15,
        text='Bar',
        command=self.bar)
    _bar.place(y=30, x=60)

    _pie = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=40, height=15,
        text='Pie',
        command=self.pie)
    _pie.place(y=30,x=120)

    _file = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=80, height=15,
        text='Datasheet',
        command=self.browseFiles)
    _file.place(y=30,x=180)

    self.root.mainloop()

  def new_window(self, event=None):
    if len(self.tabs) < 10:
      _window = self.Window(self.root)
      _tab = tkin.Button(
        self.root,
        image = self.pic,
        compound = 'c',
        width=40, height=15,
        text=str(len(self.tabs) + 1),
        command=lambda:self.switch_window(None, _window))

      self.tabs[_window] = _tab

      self.switch_window(None, _window)

      _tab.grid(
          row=0, column=len(self.tabs)-1)
      self.button_new.grid(
          row=0, column=10)

  def remove_window(self, event=None):
    if len(self.tabs) > 1:
      self.current_tab.destroy()
      self.current_window.get_tk_widget().destroy()
      self.tabs.pop(self.current_window)



  def switch_window(self, event=None, tab=0):
    self.current_tab = self.tabs[tab]
    self.current_window = tab

    for window in self.tabs:
      if window == tab:
        window.get_tk_widget().place(
            anchor='center',
            relx=0.5, rely=0.5,
            relwidth=0.8, relheight=0.8)
        self.tabs[window]['bg'] = '#f1f1f1'
      else:
        window.get_tk_widget().place_forget()
        self.tabs[window]['bg'] = '#cecece'


  def standard(self):
    try:
      data = self.file['points']
      self.current_window.fig.clear()
      self.current_window.fig.add_subplot(111).plot(data)
      self.current_window.draw()
    except:
      pass

  def bar(self):
      width = self.file['country'].tolist()
      height = self.file['points'].tolist()

      dictionary: dict = {}

      for item in width:
        try:
          if not item in dictionary:
            dictionary[item] = height.pop(0)
          else:
            dictionary[item] = round((dictionary[item] + height.pop(0)) / 2)
        except ValueError:
          print("Invalid Value")
        except TypeError:
          print("Invalid Type")


      x_values: list = []
      y_values: list = []

      dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

      for item in dictionary:
        x_values.append(item[0])
        y_values.append(item[1])

      y_pos = np.arange(len(x_values))

      self.current_window.fig.clear()
      self.current_window.fig.add_subplot(111).bar(y_pos, y_values)
      self.current_window.draw()

  def pie(self):
      name = self.file['country'].tolist()
      data = self.file['points'].tolist()
      dictionary: dict = {}

      for item in name:
        try:
          if not item in dictionary:
            dictionary[item] = data.pop(0)
          else:
            dictionary[item] = round((dictionary[item] + data.pop(0)) / 2)
        except ValueError:
          print("Invalid Value")
        except TypeError:
          print("Invalid Type")


      x_values: list = []
      y_values: list = []

      dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

      for item in dictionary:
        x_values.append(item[0])
        y_values.append(item[1])

      self.current_window.fig.clear()
      self.current_window.fig.add_subplot(111).pie(y_values)
      self.current_window.draw()

  def browseFiles(self):
    filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Select a File",
        filetypes = (
            ("CSV files", "*.csv*"),
            ("All Files", "*.*")))

    try:
      self.file = pd.read_csv(filename)
    except UnicodeDecodeError:
      print('Invalid file type!')









if __name__ == '__main__':

  GRAPH_WIDGET = MainWindow()