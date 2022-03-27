import random
random.seed(10)
l_score=0
for i in range(5):
    l_1 = random.randint(1, 100)
    l_2 = random.randint(1, 100)
    l_input=int(input('{}+{}='.format(l_1,l_2)))
    l_result=l_1+l_2
    if l_input==l_result:
        l_score+=1
        if l_score>=4:
            print('闯关成功')
        else:
            print('闯关不成功')