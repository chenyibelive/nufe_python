sex=input("请输入您的性别(M或者F): ")
age=int(input("请输入您的年龄(1-120) : "))
if sex=='M':
    if age >= 22:
        print("到达合法结婚年龄")
    else:
        print("未到合法结婚年龄")
else:
    if age >= 20:
        print("到达合法结婚年龄")
    else:
        print("未到合法结婚年龄")


first=eval(input("请输入第一个数字:"))
second=eval(input("请输入第二个数字:"))
sign=input("请输入运算符号:")
if sign=='+':
    print("两数之和为:0".format(first+second))
elif sign=='-':
    print("两数之差为:f".format(first-second))
elif sign=='*':
    print("两数之积为:f".format(first*second))
elif sign=='/':
    if second!=0:
        print("两数之商为:{}".format(first/second))
    else:
        print("除数为0错误!")
else:
    print("符号输入有误! ")

