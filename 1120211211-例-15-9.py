from tkinter import *
def draw(event):
	mycanvas.create_rectangle(90,10,200,200)
	mycanvas.create_oval(90,10,200,200,fill='green')
	mycanvas.create_arc(90,10,200,200,fill='pink')
	mycanvas.create_polygon(20,180,150,10,290,180, outline='blue',fill='')
	mycanvas.create_line(10,105,290,105,fill='red')
	mycanvas.create_text(50,10,text='我的画布',fill='#123456')
def delt():
	mycanvas.delete(ALL)
root=Tk()
root.geometry('320x240')
mycanvas=Canvas(root,width=300,height=200)
mycanvas.bind('<ButtonPress-1>',draw)
mycanvas.pack()
btnclear=Button(root,text='清空',command=delt)
btnclear.pack()
root.mainloop()
