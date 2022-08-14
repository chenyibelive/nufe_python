path1="score.txt"
f1=open(path1,'r',encoding="utf-8")
for line1 in f1.readlines():
	newline1=line1.rstrip()
	newwords1=newline1.split(" ")
	print(newwords1)
f1.close