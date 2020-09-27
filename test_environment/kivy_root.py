from kivy.app import App
from kivy.uix.widget import Widget


class RootApp(App):
	def build(self):
		return WindowWidget()




class WindowWidget(Widget):
	pass


if __name__ == '__main__':
	RootApp().run()