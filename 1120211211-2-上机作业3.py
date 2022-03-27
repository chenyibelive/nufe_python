n = int(input("请输入一个正整数n:"))
if n < 2:           #判断是否大于1的整数，且1不是素数
    print("%d不是素数！"%n)
else:
    for i in range(2,n):
        if n % i == 0:    #判断2——i是否有能被整除
            print("%d不是素数！"%n)
            break
    else:
        print("%d是素数！"%n)