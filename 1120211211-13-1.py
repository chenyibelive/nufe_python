from tkinter import *

# 设置登录窗口
win = Tk()
win.title('登陆')
win.geometry('300x150')
win.resizable(0, 0)
# 设置账号
Label(text='账号:').place(x=50, y=30)
uname = Entry(win)
uname.place(x=100, y=30)
# 设置密码
Label(text='密码:').place(x=50, y=70)
pwd = Entry(win)
pwd.place(x=100, y=70)
# 登陆
def login():
    username = uname.get()
    password = pwd.get()
    if username == 'abc' and password == '123':
        s="登陆成功"
    elif username == 'abc' and password != '123':
        s='密码错误'
    else:
        s="用户不存在"
    lb2.configure(text = s)
# 登陆按钮
Button(text='登陆', command=login).place(x=100, y=110)
lb2=Label(win, text ="")
lb2.pack()


win.mainloop()