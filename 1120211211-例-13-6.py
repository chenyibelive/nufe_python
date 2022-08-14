import tkinter
import time
def gettime():
	timestr = time.strftime("%H:%M:%S")
	var.set(timestr)
	root.after(1000,gettime)
root = tkinter.Tk()
root.title("时钟")
var=tkinter.StringVar()
lb = tkinter.Label(root, textvariable=var, fg = 'black', font =('黑体',80))
lb.pack()
gettime()
root.mainloop()
