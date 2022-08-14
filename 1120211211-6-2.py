years = eval(input('请输入年份：'))
if(years%100 != 0 | years%4 == 0):
    print('是闰年')
elif(years%400 == 0):
    print('是闰年')
else:
    print('不是闰年')