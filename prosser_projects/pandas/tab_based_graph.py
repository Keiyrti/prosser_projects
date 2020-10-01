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

  def __init__(self, canvas, figure, tab, title=None):
    self.canvas = canvas
    self.fig = figure
    self.tab = tab
    self.title = title

    self.x = [0, 1, 2, 3]
    self.y = [0, 1, 2, int(tab['text'])]

  def __repr__(self):
    return self.title

  def graph(self, x_title=None, y_title=None):
    x_data = list(self.x)
    y_data = list(self.y)

    self.fig.clear()

    graph = self.fig.add_subplot(111)

    graph.plot(x_data, y_data)
    self.canvas.draw()

  def bar(self):
    pass

  def pie(self):
    pass


# Root Creation
root = tkin.Tk()
root.minsize(800, 450)

assets = []
curr_asset = None

invis_pic = tkin.PhotoImage(width=1, height=1)


left_panel = tkin.Frame(
    root,
    bg='#d1d1d1',
    width=450, height=450)
left_panel.grid(row=0, column=0)

middle_panel = tkin.Frame(
    root,
    bg="#1e1e1e",
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
    font=20)
graph_title.place(
    anchor='n',
    relx=0.5,y=20)

tabs_frame = tkin.Frame(
    left_panel,
    width=30, height=360)
tabs_frame.place(
    anchor='ne',
    x=60, rely=1,
    y=-390)

graph_figure = Figure(figsize=[4, 4], dpi=90)

graph = FigureCanvasTkAgg(
    graph_figure,
    left_panel)
graph.get_tk_widget().place(
    anchor='s',
    relx=0.5, rely=1,
    x=15, y=-30)

def new_window():
  tab = tkin.Button(
    tabs_frame,
    image=invis_pic,
    compound='c',
    width=30, height=20,
    relief='flat',
    text=str(len(assets) + 1))
  tab.bind("<Button-1>", switch_window)

  tab.grid(
      row=len(assets), column=0)
  figure = Window(graph, graph_figure, tab, f'Graph {len(assets) + 1}')
  figure.graph()
  graph_title['text'] = figure.title

  assets.append(figure)
  global curr_asset
  curr_asset = figure

def delete_window():
  global assets
  global curr_asset
  if len(assets) != 1:
    _removed = curr_asset.tab['text']
    curr_asset.tab.destroy()
    assets.remove(curr_asset)

    for obj in assets:
      obj.tab['text'] = assets.index(obj) + 1
      obj.tab.grid_configure(
          row=assets.index(obj), column=0)

    if _removed == '1':
      print('gone')
      index = 0
    else:
      index = int(_removed) - 2

    obj = assets[index]
    obj.graph()
    graph_title['text'] = obj.title
    curr_asset = obj
  else:
    pass


def switch_window(window):
  index = int(window.widget['text']) - 1
  obj = assets[index]
  obj.graph()
  graph_title['text'] = obj.title
  global curr_asset
  curr_asset = obj

new_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    compound='c',
    width=30, height=20,
    relief='flat',
    text='+',
    command=new_window)
new_button.place(
    anchor='n',
    relx=0.5, rely=1,
    y=-50)

delete_button = tkin.Button(
    middle_panel,
    image=invis_pic,
    compound='c',
    width=30, height=20,
    relief='flat',
    text='-',
    command=delete_window)
delete_button.place(
    anchor='s',
    relx=0.5, rely=1,
    y=-50)

new_window()
root.mainloop()