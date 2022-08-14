from tkinter import *
root=Tk()
root.geometry('320x240')
mycanvas=Canvas(root,bg='red',height=200,width=280)
mycanvas.pack()
btn1=Button(root,text='关闭',command=root.destroy)
btn1.pack()
root.mainloop()
