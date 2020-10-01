import tkinter as tkin

root = tkin.Tk()

string = tkin.StringVar()

entry = tkin.Entry(
    root,
    text=string)
entry.pack()

label = tkin.Button(
    text='print',
    command=lambda:print(string.get()))
label.pack()

root.mainloop()