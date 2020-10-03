from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer # Позволяет подсвечивать текст HTML
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout # Плавающее окно
from kivy.uix.scatter import Scatter # Позволяет двигать пальцами тач

Config.set('graphics', 'resizable', '0'); # Не позволяет изменить размер окна
Config.set('graphics', 'width', '2560');
Config.set('graphics', 'height', '1440');

class MyApp(App):
	def build (self):
		#return CodeInput (lexer = HtmlLexer())
		#return Button(text="Hello")
		s = Scatter()
		#return CodeInput(lexer = HtmlLexer())
		fl = FloatLayout(size = (600, 600))
		s.add_widget(fl)
		fl.add_widget(Button(text = 'It\'s my first button!',
			                 font_size=30, 
			                 on_press = self.btn_press, # Метод, который указывает, что делать, если нажата кнопка
			                 background_color = [1,0,0,1], # Задает цвет кнопки
			                 background_normal = ' ',
			                 size_hint = (.5, .25), #  Указывает процент размера кнопки относительно Layout
		                     pos = (2560/2 - 1280/2, 1440/2 - 144) ) ); # Позиция кнопки
		'''return Button (text="Hello!", 
			           font_size=30, 
			           on_press = self.btn_press, 
			           background_color = [11,0,2,1],
			           background_normal = '') '''
		return s #f1	           

	def btn_press(self, instance):	
		print('Button is pressed')
		instance.text = 'I\'m  pressed!' # Смена текста кнопки

if __name__ == "__main__":
	MyApp().run()