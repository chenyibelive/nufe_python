import tkinter
def run():
	if CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0:
		s ="您没有选择任何爱好项目"
	else:
		s1 = s2 = s3 = s4 = ""
		if CheckVar1.get()==1:
			s1 ="足球"
		if CheckVar2.get()==1:
			s2 ="篮球"
		if CheckVar3.get()==1:
			s3="游泳"
		if CheckVar4.get()==1:
			s4="田径"
		s ="您选择了{}{}{}{}".format(s1,s2,s3,s4)
	lb2.configure(text = s)

root = tkinter.Tk()
root.title("复选GUI")
lb = tkinter.Label(root, text="请选择您的爱好项目:")
lb.pack()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
CheckVar3 = tkinter.IntVar()
CheckVar4 = tkinter.IntVar()
ch1 = tkinter.Checkbutton(root, text = "足球" , variable = CheckVar1, onvalue = 1, offvalue = 0)
ch1.pack()
ch2 = tkinter.Checkbutton(root, text = "篮球" ,variable = CheckVar2, onvalue = 1, offvalue = 0)
ch2.pack()
ch3 = tkinter.Checkbutton(root, text ="游泳", variable = CheckVar3, onvalue = 1, offvalue = 0)
ch3.pack()
ch4 = tkinter.Checkbutton(root, text ="田径",variable = CheckVar4, onvalue = 1, offvalue = 0)
ch4.pack()
btn = tkinter.Button(root, text="OK", command=run)
btn.pack()
lb2 = tkinter.Label(root, text="")
lb2.pack()
root.mainloop()
