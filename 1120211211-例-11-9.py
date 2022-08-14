import random
def jinriyunshi(xingzuo, year, month, day):
	count = year * 11 + month * 7 + day * 5
	for c in xingzuo:
		count += ord(c)
	random.seed(count)
	a = random.randint(1,5)
	b = random.randint(1,5)
	c = random.randint(1,5)
	d = random.randint(1,5)
	e = random.randint(1,5)
	return a, b, c, d, e
while True:
	xingzuo = input("请输入您的星座:")
	a, b,c,d,e = jinriyunshi(xingzuo,2018,4,26)
	print("星座:{}".format(xingzuo))
	print("整体运势:{}".format('*'*a))
	print("爱情运势:{}".format('*'*b))
	print("事业运势:{}".format('*'*c))
	print("财富运势:{}".format('*'*d))
	print("健康运势:{}".format('*'*e))
