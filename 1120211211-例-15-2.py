from tkinter import *
import math
root = Tk()
w =Canvas(root, width=320, height=240)
w.pack()
w0=160
h0=120
w.create_line(0,120,320,120,fill="red", arrow=LAST)
w.create_line(160,240,160,0,fill="red", arrow=LAST)
w.create_text(w0+50,10,text='y=sin(x)')
for i in range(-3,4):
	j=i*40
	w.create_line(j+w0, h0,j+w0, h0-5,fill="red")
	w.create_text(j+w0,h0+5,text=str(i))

for i in range(-2,3):
	j=i*40
	w.create_line(w0,j+h0, w0+5,j+h0,fill="red")
	w.create_text(w0-10,j+h0,text=str(-i))

def x(t):
	x =t*40
	x+=w0
	return x
def y(t):
	y = math.sin(t)*40
	y-=h0
	y =-y
	return y
t = -math.pi
while(t<math.pi):
	w.create_line(x(t),y(t),x(t+0.01),y(t+0.01),fill="blue")
	t+=0.01
root.mainloop()
