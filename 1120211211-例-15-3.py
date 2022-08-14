from tkinter import*
import math
root = Tk()
w= Canvas(root, width=600, height=600)
w.pack()
w.create_line(0,300,600,300,fill="red", dash=(4,4))
w.create_line(300,0,300,600,fill="red", dash=(4,4))
w0=300
h0=300
def x(t):
 	x=(w0/32)*(math.cos(t)-t*math.sin(t))
 	x+=w0
 	return x
def y(t):
	y =(h0/ 32)*(math.sin(t)+t* math.cos(t))
	y-=h0
	y =-y
	return y
t = 0.0
while(t<25):
	w.create_line(x(t),y(t),x(t+0.01),y(t+0.01),fill="blue")
	t+=0.01
root.mainloop()
