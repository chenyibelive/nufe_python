name=input("请输入您的姓名: ")
age=int(input("请输入您的年龄: "))
if age <= 0:
    print("{}年龄输入错误".format(name))
elif age>=18:
    print("{}已经成年".format(name))
    print("欢迎欢迎，请上网")
else:
    print("{}还未成年".format(name))
    print("回家吧，回到最初的美好")
