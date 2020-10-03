from kivy.app import App
from kivy.uix.button import Button # Импорт кнопки
#from kivy.uix.boxlayout import BoxLayout # Все лэйауты юикс
from kivy.uix.gridlayout import GridLayout # Layout "таблица"
from kivy.uix.anchorlayout import AnchorLayout # Позволяет поместить виджет а в одну из 9 сторон

class BoxApp(App):
	def build(self):
		#bl = BoxLayout(orientation = 'vertical', padding = [20,20], spacing = 0) # Ориентация, отступ и пространство между кнопками
		#bl = GridLayout(cols=5, rows = 5, padding = [20,20], spacing = 3) # rows - задает количество строк, а col - количество колон
		bl = AnchorLayout(anchor_x = 'center', anchor_y = 'center' ) # Ориентация кнопки в пространстве, 9 точек
		bl.add_widget(Button(text = 'O_o', size_hint=[.25, .25]))

		'''for x in range(25):
		    bl.add_widget(Button(text = '{X_X}')) # Добавляем виджет "кнопку" в layout, с текстом 'Button 1'''

		return bl

	def btn_press(self, instance):
		print('Button is pressed')
		instance.text = 'I\'m  pressed!'

if __name__ == "__main__":
	BoxApp().run()