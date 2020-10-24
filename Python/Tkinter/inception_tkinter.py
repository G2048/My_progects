from tkinter import*
from tkinter import messagebox
import tempfile, base64, zlib

root = Tk() #global object# window of application

def remove_icon():
	ICON = zlib.decompress(base64.b64decode('eJxjYGAEQgEBBiDJwZDBy'
	    'sAgxsDAoAHEQCEGBQaIOAg4sDIgACMUj4JRMApGwQgF/ykEAFXxQRc='))
	_, ICON_PATH = tempfile.mkstemp()
	with open(ICON_PATH, 'wb') as icon_file:
	    icon_file.write(ICON)
	root.iconbitmap(default=ICON_PATH)
	label = Label(root, text="Window with transparent icon.")
	label.pack()


def btn_click():
	login = loginInput.get() # data interception 
	password = passField.get() # data interception

	info_str = f'Data: {str(login)}, {str(password)}'
	messagebox.showinfo(title = 'Name of', message = info_str) #information output
	messagebox.showerror(title = '', message = 'Error!!!')


#root.iconbitmap(r'c:\\Python32\\DLLs\\py\.ico')
remove_icon()

root['bg'] = '#fafafa' #background of window
root.title('Name of programm')
#root.wm_attributes('-alpha', 0.7) #window transparency
root.geometry('600x500') #size of window

root.resizable(width=False, height=False) #window resizing prohibition

canvas = Canvas(root, height=300, width=250) #canvas for drawing
canvas.pack()

frame = Frame(root, bg='red') #a frame containing other visual components
frame.place(relx=0.15, rely=0.15 ,relwidth=0.7, relheight=0.7) # relx - window offset; relwidth - size of window in % !

title = Label(frame, text = 'Text is cheetsheet', bg = 'gray', font = 40)
title.pack() #pack,grid or place - for to addition widgets to a window (frame)
btn = Button(frame, text = 'This is Button!', bg = 'green', command = btn_click)
btn.pack()

loginInput = Entry(frame, bg = 'white') #text input field
loginInput.pack()

passField = Entry(frame, bg = 'white', show = '*')
passField.pack()

root.mainloop() #EVREFING!