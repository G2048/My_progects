from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from random import random
from kivy.graphics import (Color, Ellipse, Line, Rectangle) # Импорт графических настроек
from kivy.core.window import Window

class PainterWidget(Widget):
	'''def __init__(self, **kwargs):
		super(PainterWidget, self).__init__(**kwargs)

		with self.canvas:
			Color (0,1,0,1)
			Ellipse (pos = (touch.x-rad/2, touch.y-rad/2), size=(rad,rad)) # pos - position in space '''

			#self.line = Line (points = ( ), width = 2, joint = 'miter', cap = 'square')
			#self.line = Line (points = (100,100, 150,200, 200,100), close = True, width = 2) # построение отрезков по точкам; close - "закрывает" линии в фигуру;
			# width - задает ширину линии; joint (none,bevel,miter, round)- указывает каким должен быть "перелом" одной линии с другой
			# cap (square, round) - указывает должны ли быть закругленны начало и конец линий
	def on_touch_down (self, touch):
		#self.line.points += (touch.x, touch.y) # Дополнение линий точками
		with self.canvas:
			Color (random() ,random() ,random() ,random())
			rad = 30
			Ellipse (pos = (touch.x-rad/2, touch.y-rad/2), size=(rad,rad)) # pos - position in space
			touch.ud['line'] = Line (points = (touch.x, touch.y), width = 15) # ud - словарь пользователя

	def on_touch_move (self, touch):
		touch.ud ["line"].points += (touch.x, touch.y)


class PaintApp(App):
	def build (self):
		parent = Widget ()
		self.painter = PainterWidget()
		parent.add_widget(self.painter)
		parent.add_widget (Button(text = 'Clear' , on_press = self.clear_canvas, size=(100, 50)))
		parent.add_widget (Button(text = 'Save' , on_press = self.save, size=(100, 50), pos=(100, 0)))
		parent.add_widget (Button(text = 'Screen' , on_press = self.screen, size=(100, 50), pos=(200, 0)))

		return parent
	def clear_canvas (self, instance):
		self.painter.canvas.clear()

	def save (self, instance):
		self.painter.size = (Window.size [0], Window.size [1]) # Увеличивает размер сохраняемого окна; В ячейке 1 - высота окна, во 2 - ширина
		self.painter.export_to_png('image.png') # Сохраняет рисунок
	def screen (self, instance):
		Window.screenshot('screen.png')

if __name__ == "__main__":
	PaintApp().run()