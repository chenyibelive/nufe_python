username=input("请输入您的用户名:")
password=input("请输入您的密码:")
if username=="admin":
    if password=="123456":
        print("输入正确，恭喜进入! ")
    else:
        print("密码有误，请重试!")
else:
    print("用户名有误，请重试!")

import random
randnumber=random.randint(1,10)
guess=int(input("请输入您的猜测:"))
print("随机数为:".format(randnumber))
if guess>randnumber:
    print("您的猜测太大")
elif guess<randnumber:
    print("您的猜测太小")
else:
    print("恭喜您猜对了")

