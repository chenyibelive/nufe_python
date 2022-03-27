w=eval(input())

if w<=220:
    x=w*3.45
    print('{:.1f}'.format(x))

if 220<w<=300:
    x=(w-220)*4.83+220*3.45
    print('{:.1f}'.format(x))
if w>300:
    x=(w-300)*5.83+80*4.83+220*3.45
    print('{:.1f}'.format(x))