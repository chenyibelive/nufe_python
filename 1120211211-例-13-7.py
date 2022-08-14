from tkinter import *
import datetime
def gettime():
	s = "{}\n".format(str(datetime.datetime.now()))
	txt.insert(END, s)
	root.after(1000, gettime)
root = Tk()
root.geometry('320x240')
txt = Text(root)
txt.pack()
gettime()
root.mainloop()
