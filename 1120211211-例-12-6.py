class MyClass:
	i=12345
	def f(self):
		return 'hello world'

if __name__=="__main__":

	myc=MyClass()

	print(myc.i)
	print(myc.f())