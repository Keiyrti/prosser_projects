from tkinter import *

expression = ""

class Button(Button):
  def __init__(self, master, cnf=[], **kw):
    super().__init__(master, cnf, **kw)
    self.invis_pic = PhotoImage(width=1, height=1)
    self['image'] = self.invis_pic
    self['compound'] = 'c'
    self['width'] = 64
    self['height'] = 64
    self['font'] = ('Helvetica', 16)

def press(num):
  global expression
  expression = expression + str(num)

  equation.set(expression)

def equalpress():
  try:
    global expression
    total = str(eval(expression))
    equation.set(total)
    expression = ""
  except:
    equation.set(" error ")
    expression = ""

def clear():
  global expression
  expression = ""
  equation.set("")

if __name__ == "__main__":
  root = Tk()
  root.title("Calculator")
  invis_pic = PhotoImage(width=1, height=1)
  equation = StringVar()
  expression_field = Label(
    root, textvariable=equation,
    image=invis_pic,
    compound='c',
    relief='sunken',
    height=64,
    font=('Helvetica', 16))
  expression_field.grid(columnspan=4, ipadx=5, sticky='ew')
  equation.set('enter your expression')
  button1 = Button(
    root, text=' 1 ',
    command=lambda: press(1))
  button1.grid(row=2, column=0)

  button2 = Button(
    root, text=' 2 ',
    command=lambda: press(2))
  button2.grid(row=2, column=1)

  button3 = Button(
    root, text=' 3 ',
    command=lambda: press(3))
  button3.grid(row=2, column=2)

  button4 = Button(
    root, text=' 4 ',
    command=lambda: press(4))
  button4.grid(row=3, column=0)

  button5 = Button(
    root, text=' 5 ',
    command=lambda: press(5))
  button5.grid(row=3, column=1)

  button6 = Button(
    root, text=' 6 ',
    command=lambda: press(6))
  button6.grid(row=3, column=2)

  button7 = Button(
    root, text=' 7 ',
    command=lambda: press(7))
  button7.grid(row=4, column=0)

  button8 = Button(
    root, text=' 8 ',
    command=lambda: press(8))
  button8.grid(row=4, column=1)

  button9 = Button(
    root, text=' 9 ',
    command=lambda: press(9))
  button9.grid(row=4, column=2)

  button0 = Button(
    root, text=' 0 ',
    command=lambda: press(0))
  button0.grid(row=5, column=0)

  plus = Button(
    root, text=' + ',
    command=lambda: press("+"))
  plus.grid(row=2, column=3)

  minus = Button(
    root, text=' - ',
    command=lambda: press("-"))
  minus.grid(row=3, column=3)

  multiply = Button(
    root, text=' * ',
    command=lambda: press("*"))
  multiply.grid(row=4, column=3)

  divide = Button(
    root, text=' / ',
    command=lambda: press("/"))
  divide.grid(row=5, column=3)

  equal = Button(
    root, text=' = ',
    command=equalpress)
  equal.grid(row=5, column=2)

  clear = Button(
    root, text='Clear',
    command=clear)
  clear.grid(row=5, column='1')

  Decimal= Button(
    root, text='.',
    command=lambda: press('.'))
  Decimal.grid(row=6, column=0)

  root.mainloop()