#复合赋值语句
x, y = 1,1.5
print("x:{} ".format(x))
print("y:{} ".format(y))

#多目标赋值
first = second = third = "welcome"
print("first:{}".format(first))
print("second:{}".format(second))
print("third:{}".format(third))

#复合赋值
age = 10
print("first age:{}".format(age))
age += 3
print("second age:{}".format(age))

#编写程序，从键盘输入语文、数学、英语三门功课的成绩，计算并输出平均成绩，要求平均成绩小数点后保留1位。
chinese=float(input("请输入您的语文成绩:"))
math=float(input("请输入您的数学成绩:"))
english=float(input("请输入你的英语成绩:"))
average=( chinese + math + english)/3
print("您的平均成绩为{:.1f},".format(average))

chinese=eval(input("请输入您的语文成绩:"))
math=eval(input("请输入您的数学成绩:"))
english=eval(input("请输入你的英语成绩:"))
average=(chinese + math + english)/3
print("您的平均成绩为{:.1f},".format(average))



