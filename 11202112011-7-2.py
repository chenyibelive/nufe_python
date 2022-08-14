num = 100
while num>=100 and num <1000:
    a = num//100
    b = (num-a*100)//10
    c = num - a*100 - b*10

    if (a**3 + b**3 + c**3 ==num):
        print(num)
    num = num+1

