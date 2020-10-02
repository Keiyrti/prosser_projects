'''Matploblib based tkinter window with tabbable figures.'''

import tkinter as tkin

import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Window():
  '''Window management and storage.'''

  def __init__(self, tab, title=None):
    self.fig = Figure(figsize=[5, 4], dpi=80)
    self.canvas = FigureCanvasTkAgg(
        self.fig,
        left_panel)
    self.canvas.get_tk_widget().place(
        anchor='s',
        relx=0.5, rely=1,
        x=15, y=-30)
    self.tab = tab
    self.title = title

  def __repr__(self):
    return self.title

  def graph(self, x_title=None, y_title=None):
    if file == None:
      self.x = [1, 2, 3, 4]
      self.y = [4, 2, 1, 3]
      x_data = list(self.x)
      y_data = list(self.y)
    else:
      self.x = list(file[x_name.get()])
      self.y = list(file[y_name.get()])
      x_data = list(self.x)
      y_data = list(self.y)

    self.fig.clear()

    graph = self.fig.add_subplot(111)

    graph_figure = self.fig

    graph.plot(x_data, y_data)
    self.canvas.draw()

  def bar(self):
    self.fig.clear()
    if file == None:
      self.x = [1, 2, 3, 4]
      self.y = [4, 2, 1, 3]
      x_data = list(self.x)
      y_data = list(self.y)
    else:
      self.x = list(file[x_name.get()])
      self.y = list(file[y_name.get()])
      x_data = list(self.x)
      y_data = list(self.y)

    graph = self.fig.add_subplot(111)
    graph.set_xlabel("X Values")
    graph.set_ylabel("Y Values")

    graph.bar(x_data, y_data)
    self.canvas.draw()

  def pie(self):
    if file == None:
      self.x = [1, 2, 3, 4]
      self.y = [4, 2, 1, 3]
      x_data = list(self.x)
      y_data = list(self.y)
    else:
      self.x = list(file[x_name.get()])
      self.y = list(file[y_name.get()])
      x_data = list(self.x)
      y_data = list(self.y)

    self.fig.clear()

    graph = self.fig.add_subplot(111)

    graph.pie(y_data, normalize=True)
    self.canvas.draw()


# Root Creation
root = tkin.Tk()
root.minsize(800, 450)

assets = []
curr_asset = None

file = None

invis_pic = tkin.PhotoImage(width=1, height=1)


left_panel = tkin.Frame(
    root,
    bg='#d1d1d1',
    width=450, height=450)
left_panel.grid(row=0, column=0)

middle_panel = tkin.Frame(
    root,
    bg="#d1d1d1",
    width=30, height=450)
middle_panel.grid(row=0, column=1)

right_panel = tkin.Frame(
    root,
    bg='#d1d1d1',
    width=320, height=450)
right_panel.grid(row=0, column=2)

graph_title = tkin.Label(
    left_panel,
    bg=left_panel['bg'],
    text='Graph 1',
    font=("TkDefaultFont", 18, 'bold'))
graph_title.place(
    anchor='c',
    relx=0.5,
    x=15, y=30)

def title_change(event=None):
  _input = tkin.Entry(
      left_panel,
      bg=left_panel['bg'], fg='#8888ff',
      justify='center',
      relief='flat',
      font=("TkDefaultFont", 18, 'bold'))
  _input.insert(0, graph_title['text'])
  _input.place(
      anchor='c',
      relx=0.5,
      x=15, y=30)
  _input.focus_set()

  def confirm(event=None):
    global assets
    new_title = event.widget.get()
    curr_asset.title = new_title
    graph_title['text'] = new_title
    event.widget.destroy()

  _input.bind('<Return>', confirm)

graph_title.bind('<Button-1>', title_change)

tabs_frame = tkin.Frame(
    left_panel,
    width=30, height=360)
tabs_frame.place(
    anchor='ne',
    x=60, rely=1,
    y=-390)

def change():
  for objects in assets:
    if objects != curr_asset:
      objects.tab['bg'] = "#8888ff"
      objects.canvas.get_tk_widget().place_forget()
    else:
      objects.tab['bg'] = '#ffffff'
      objects.canvas.get_tk_widget().place(
          anchor='s',
          relx=0.5, rely=1,
          x=15, y=-30)

def new_window():
  tab = tkin.Button(
    tabs_frame,
    bg='#8888ff',
    image=invis_pic,
    compound='c',
    width=20, height=20,
    relief='flat',
    text=str(len(assets) + 1),
    font=("TkDefaultFont 12 bold"))
  tab.bind("<Button-1>", switch_window)

  tab.grid(row=len(assets), column=0)
  figure = Window(tab, f'Graph {len(assets) + 1}')
  figure.canvas.get_tk_widget().place(
      anchor='s',
      relx=0.5, rely=1,
      x=15, y=-30)
  graph_title['text'] = figure.title

  assets.append(figure)
  global curr_asset
  curr_asset = figure

  change()


def delete_window():
  global assets
  global curr_asset
  if len(assets) != 1:
    _removed = int(curr_asset.tab['text'])
    curr_asset.tab.destroy()
    curr_asset.canvas.get_tk_widget().destroy()
    assets.remove(curr_asset)

    for obj in assets:
      obj.tab['text'] = assets.index(obj) + 1
      obj.tab.grid_configure(
          row=assets.index(obj), column=0)

    if _removed == 1:
      index = 0
    else:
      index = _removed - 2

    obj = assets[index]
    graph_title['text'] = obj.title
    curr_asset = obj

    change()

  else:
    pass


def switch_window(window):
  global curr_asset
  index = int(window.widget['text']) - 1
  obj = assets[index]
  graph_title['text'] = obj.title
  curr_asset = obj

  change()


new_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    bg='#dedede',
    compound='c',
    width=30, height=20,
    relief='flat',
    text='+',
    font=("TkDefaultFont", 18),
    command=new_window)
new_button.place(
    anchor='n',
    relx=0.5, rely=1,
    y=-55)

delete_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    bg='#f1f1f1',
    compound='c',
    width=30, height=20,
    relief='flat',
    text='-',
    font=("TkDefaultFont", 18),
    command=delete_window)
delete_button.place(
    anchor='s',
    relx=0.5, rely=1,
    y=-55)


def graphPlot():
  curr_asset.graph()

def graphBar():
  curr_asset.bar()

def graphPie():
  curr_asset.pie()


graph_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    bg='#dedede',
    compound='c',
    width=30, height=20,
    relief='flat',
    text='G',
    font=("TkDefaultFont", 18),
    command=graphPlot)
graph_button.place(
    anchor='n',
    relx=0.5,
    y=60)

bar_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    bg='#f1f1f1',
    compound='c',
    width=30, height=20,
    relief='flat',
    text='B',
    font=("TkDefaultFont", 18),
    command=graphBar)
bar_button.place(
    anchor='n',
    relx=0.5,
    y=88)

pie_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    bg='#dedede',
    compound='c',
    width=30, height=20,
    relief='flat',
    text='P',
    font=("TkDefaultFont", 18),
    command=graphPie)
pie_button.place(
    anchor='n',
    relx=0.5,
    y=116)

x_name = tkin.StringVar()
y_name = tkin.StringVar()

x_label = tkin.Label(
    right_panel,
    text='X Value')
x_label.grid(row=0, column=0)

x_entry = tkin.Entry(
    right_panel,
    text=x_name)
x_entry.grid(row=0, column=1, columnspan=2)

y_label = tkin.Label(
    right_panel,
    text='Y Value')
y_label.grid(row=1, column=0)

y_entry = tkin.Entry(
    right_panel,
    text=y_name)
y_entry.grid(row=1, column=1, columnspan=2)

feedback_label = tkin.Label(
    right_panel,
    text='feedback')
feedback_label.grid(row=2, column=0, columnspan=2)

def browseFiles():
  global file
  filename = tkin.filedialog.askopenfilename(
      title = "Select a File",
      filetypes = (
          ("CSV files", "*.csv*"),
          ("All Files", "*.*")))

  try:
    file = pd.read_csv(filename)
  except UnicodeDecodeError:
    print('Invalid file type!')
  except FileNotFoundError:
    print('No file selected')

import_button = tkin.Button(
    right_panel,
    text='Import',
    command=browseFiles)
import_button.grid(row=2, column=2)



new_window()
root.mainloop()