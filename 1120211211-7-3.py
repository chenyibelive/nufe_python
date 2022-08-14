a = eval(input('请输入一个整数：'))
i=2
n=0
if a<=1:
    print('输入错误，请重新输入：')
elif a == 2:
    print('{}为素数'.format(a))
else:
    while i<a:
        if a%i == 0:
            n = n+1
        i = i + 1
if n == 0:
    print('是素数')
else:
    print('不是素数')