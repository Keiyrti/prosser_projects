from tkinter import *
root = Tk()

class RoundedWidget(Canvas):
  def __init__(self, master, cnf={'width': 150, 'height':100}, **kw):
    super().__init__(master, cnf)
    self.place(rely=1, y=-20, relx=0.5, anchor="s")
  def polygon(self, radius=25, **kwargs):
    x1 = 0
    y1 = 0
    x2 = int(self['width'])
    y2 = int(self['height'])

    points = [
        x1+radius, y1,
        x1+radius, y1,
        x2-radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1+radius,
        x1, y1]

    return self.create_polygon(points, **kwargs, smooth=True)

  def text(self, **kwargs):
    x = int(self['width']) / 2
    y = int(self['height']) / 2

    return self.create_text(x, y, **kwargs)


if __name__ == '__main__':
  my_rectangle = RoundedWidget(root)
  my_rectangle.polygon(radius=20, fill='#1e1e1e')
  my_rectangle.text(text='Hello World', fill='#f1f1f1')
  root.mainloop()