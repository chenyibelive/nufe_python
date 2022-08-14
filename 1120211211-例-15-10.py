from tkinter import *
root=Tk()
root.geometry('320x240')
mycanvas=Canvas(root)
mycanvas.pack()
photo=Photolmage(file='1.gif')
mycanvas.create_image(100,100,image=photo)
root.mainloop()
