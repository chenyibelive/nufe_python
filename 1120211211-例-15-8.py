from tkinter import *
root = Tk()
w= Canvas(root, width = 320, height = 240)
w.pack()
wO =160
h0= 120
w.create_line(10,10,320,10, fill= 'red' , arrow=LAST)
w.create_line(10,10,10,240, fill= 'red' , arrow=LAST)
w.create_text(300,20,text="x")
w.create_text(20,220,text="y")
root.mainloop()
