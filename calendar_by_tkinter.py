from tkinter import *
import calendar

#Initializing tkinter
root = Tk()

root.title("My Calendar") #Setting title of the GUI
year = 2020
myCal = calendar.calendar(year)
cal_year = Label(root, text = myCal, font = "Consolas 10 bold")
cal_year.pack() #Packing the Label widget
root.mainloop()