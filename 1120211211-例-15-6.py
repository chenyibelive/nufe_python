from turtle import *
setup(900,900,0,0)
reset()
pensize(5)

for i in range(6):
	fd(100)
	right(60)
color('red')
circle(60,steps=6)
goto(-50,200)
down()
for i in range(5):
	right(144)
	fd(400)
done()
