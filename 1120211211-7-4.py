import random

i = 0 #次数
su = 0 #两数之和
userSu = 0 #用户输入的数字
right = 0 #正确的次数
while i<5:
    a = random.randint(1,100)
    b = random.randint(1,100)
    print('第{}次的两个数为：{}，{}'.format(i+1,a,b))
    userSu = eval(input('请输入两个数的和：'))
    if userSu == a+b:
        right=right+1
    i= i+1
if right/5 >= 0.8:
    print('闯关成功，答对了：{}个'.format(right))
else:print('闯关失败,答对了：{}个'.format(right))