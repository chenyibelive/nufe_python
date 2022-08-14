from tkinter import *
def show1(event):
	lb.configure(text ="哦，你点的是左键")
def show3(event):
	lb.configure(text ="哦，你点的是右键")
root = Tk()
root.title("按键实验1")
root.geometry("200x200")
lb = Label(root, text = "")
lb.pack()
btn = Button(root, text='按钮')
btn.bind("<ButtonPress-1>" , show1)
btn.bind("<ButtonPress-3>" , show3)
btn.focus_set()
btn.pack()
root.mainloop()
