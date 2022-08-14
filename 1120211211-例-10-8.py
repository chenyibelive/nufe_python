path1="score.txt"
f1=open(path1,'r',encoding="utf-8")
for line1 in f1.readlines():
	print(line1)
f1.close