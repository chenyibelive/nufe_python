a=int(input("请输入年份："))
if (a%4==0 and a%100!=0 or a%400==0):
    print("%d是闰年"%a)
else:
    print("%d不是闰年"%a)