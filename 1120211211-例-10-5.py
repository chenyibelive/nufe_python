import jieba
path1="三国演义.txt"
f1=open(path1,"r",encoding='utf-8')
txt=f1.read()
words=jieba.lcut(txt)
counts={}
for word in words:
	if len(word)==1:
		continue
	else:
		counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
	word,count=items[i]
	print("{}==={}".format(word,count))