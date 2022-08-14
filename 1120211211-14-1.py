from tkinter import *
import tkinter
def run():
	if CheckVar1.get()==0 and CheckVar2.get()==0 and CheckVar3.get()==0 and CheckVar4.get()==0:
		s ="您没有选择任何菜品"
	else:
		s1 = s2 = s3 = s4 = ""
		s1p = s2p = s3p = s4p = 0
		if CheckVar1.get()==1:
			s1 ="汉堡包"
			s1p=12
		if CheckVar2.get()==1:
			s2 ="蛋挞"
			s2p=7
		if CheckVar3.get()==1:
			s3="猪肉卷"
			s3p=10
		if CheckVar4.get()==1:
			s4="饮料"
			s4p=5
		s ="您点了{}{}{}{},一共{}元".format(s1,s2,s3,s4,s1p+s2p+s3p+s4p)
	lb2.configure(text = s)
def zhaoling(a):
	
	
	s1 = s2 = s3 = s4 = ""
	s1p = s2p = s3p = s4p = 0
	if CheckVar1.get()==1:
		s1 ="汉堡包"
		s1p=12
	if CheckVar2.get()==1:
		s2 ="蛋挞"
		s2p=7
	if CheckVar3.get()==1:
		s3="猪肉卷"
		s3p=10
	if CheckVar4.get()==1:
		s4="饮料"
		s4p=5
	szhao ="收您{}元,找零{}元".format(a,a-(s1p+s2p+s3p+s4p))
	lb3.configure(text = szhao)
root = tkinter.Tk()
root.geometry("300x300")
root.title("自助选餐")
lb = tkinter.Label(root, text="您好，请问需要什么？")
lb.pack()
CheckVar1 = tkinter.IntVar()
CheckVar2 = tkinter.IntVar()
CheckVar3 = tkinter.IntVar()
CheckVar4 = tkinter.IntVar()
ch1 = tkinter.Checkbutton(root, text = "汉堡包：12元" , variable = CheckVar1, onvalue = 1, offvalue = 0)
ch1.pack()
ch2 = tkinter.Checkbutton(root, text = "蛋挞：7元" ,variable = CheckVar2, onvalue = 1, offvalue = 0)
ch2.pack()
ch3 = tkinter.Checkbutton(root, text ="猪肉卷：10元", variable = CheckVar3, onvalue = 1, offvalue = 0)
ch3.pack()
ch4 = tkinter.Checkbutton(root, text ="饮料：5元",variable = CheckVar4, onvalue = 1, offvalue = 0)
ch4.pack()
btn = tkinter.Button(root, text="OK", command=run)
btn.pack()
lb2 = tkinter.Label(root, text="")
lb2.pack()
inp1=Entry(root)
inp1.pack()
btn2 = tkinter.Button(root, text="付款", command=lambda:zhaoling(eval(inp1.get())))
btn2.pack()
lb3 = tkinter.Label(root, text="")
lb3.pack()
root.mainloop()
