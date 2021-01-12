import tkinter as tkin
from random import randint

response = ["It is so.", "Perhaps.", "In time.", "Certainly.", "Yes.", "No.", "Unlikely.", "Uncertain.", "Impossible.", "Possible."]

root = tkin.Tk()

invis_pic = tkin.PhotoImage(width=1, height=1)

input_box = tkin.Entry(root, width=42)
input_box.grid(row=0, column=0)

ball = tkin.Canvas(
  root,
  width=360, height=360)
ball.grid(row=1, column=0,
  columnspan=2)

def ball_reset():
  ball.create_oval(20, 20, 340, 340, fill='#1e1e1e')
  ball.create_oval(80, 80, 280, 280, fill='#000000')
  ball.create_polygon(100, 230, 180, 90, 260, 230, fill="blue")

def ask():
  ball_reset()
  if input_box.get() == '':
    pass
  else:
    rand_choice = randint(0, len(response)-1)
    ball.create_text(180, 180, text=response[rand_choice], fill="white")

ask_button = tkin.Button(root, text='Ask', command=ask)
ask_button.grid(row=0, column=1, sticky='ew', padx=2, pady=2)

ball_reset()
root.mainloop()