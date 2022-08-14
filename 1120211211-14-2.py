from tkinter import *
import tkinter
from tkinter.simpledialog import *
money=0
def show1(enent):
	global money
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
	money=s1p+s2p+s3p+s4p
	
def show3(event):
	vippass=askstring('会员付款界面','请输入会员码')
	global money
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
	total=s1p+s2p+s3p+s4p
	if vippass=='vip':
		s ="您点了{}{}{}{},一共{}元,折扣价为{:.1f}元".format(s1,s2,s3,s4,total,0.8*total)
		money=0.8*total
	else:
		s ="您点了{}{}{}{},一共{}元".format(s1,s2,s3,s4,total)

		money=total
	lb2.configure(text = s)
	
def zhaoling(a,money):
	
	
	
	szhao ="收您{}元,找零{:.1f}元".format(a,a-money)
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
btn = tkinter.Button(root, text="OK")
btn.bind("<ButtonPress-1>" , show1)
btn.bind("<ButtonPress-3>" , show3)

btn.pack()
lb2 = tkinter.Label(root, text="")
lb2.pack()
print(money)
inp1=Entry(root)
inp1.pack()
btn2 = tkinter.Button(root, text="付款", command=lambda:zhaoling(eval(inp1.get()),money))
btn2.pack()
lb3 = tkinter.Label(root, text="")
lb3.pack()
root.mainloop()
print(money)
