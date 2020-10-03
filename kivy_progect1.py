from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
	def build(self):
		b1 = BoxLayout(orientational = 'horizontal')
		b1.add_widget(Button(text = 'Button 1'))
		b1.add_widget(Button(text = 'Button 2'))
		b1.add_widget(Button(text = 'Button 3'))
		return b1
	def btn_press(self, instance):
		print('Button is pressed')
		instance.text = 'I\'m  pressed!'	    

if __name__ == "__name__":
	BoxApp().run()