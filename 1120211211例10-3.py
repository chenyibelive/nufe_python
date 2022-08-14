path1="lemontree.txt"
f1=open(path1,"r",encoding='utf-8')
content=f1.read()
content=content.lower()
for ch in [',',':','?','.']:
	content=content.replace(ch," ")

words=content.split()
counts={}

for word in words:
	counts[word]=counts.get(word,0)+1

items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(10):
	word,count=items[i]
	print("{}==={}".format(word,count))
