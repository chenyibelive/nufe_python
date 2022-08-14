class Dog:
	kind = '藏獒'
	def __init__(self, name):
		self.name = name
d = Dog('Fido')
e = Dog('Buddy')
print("小狗1的种类是:{}".format(d.kind))
print("小狗2的种类是:{}".format(e.kind))
print("小狗1的名字是:{}".format(d.name))
print("小狗2的名字是:{}".format(e.name))
