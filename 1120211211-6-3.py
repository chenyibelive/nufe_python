a = eval(input('请输入a的值：'))
b = eval(input('请输入b的值：'))
c = eval(input('请输入c的值：'))
delta = b*b - 4*a*c
if delta<0:
    print('该方程无解')
elif delta == 0:
    x = 2
    print('该方程有唯一解,解为：{}'.format(x))
elif delta > 0:
    x1 = 1
    x2 = 3
    print('该方程有两个解，一个解为：{}，另外一个解为：{}'.format(x1,x2))

