from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter # Позволяет двигать пальцами тач

Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '2560');
Config.set('graphics', 'height', '1440');

class MyApp(App):
	def build (self):
		s = Scatter () 
		#return CodeInput(lexer = HtmlLexer())
		f1 = FloatLayout(size = (600, 600))
		s.add_widget(f1)
		f1.add_widget(Button(text = 'It\'s my first button!',
			                 font_size=30, 
			                 on_press = self.btn_press, 
			                 background_color = [11,0,2,1],
			                 background_normal = '',
			                 size_hint = (.5, .25), # Проценты!!!
		                     pos = (2560/2 - 1280/2,1440/2 - 1440/10) ) )
		'''return Button (text="Hello!", 
			           font_size=30, 
			           on_press = self.btn_press, 
			           background_color = [11,0,2,1],
			           background_normal = '') '''
		return s #f1	           

	def btn_press(self, instance):	
		print('Button is pressed')
		instance.text = 'I\'m  pressed!'

if __name__ == "__main__":
	MyApp().run()