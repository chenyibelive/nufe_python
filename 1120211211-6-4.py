#水费计算
sumWater = 0
water = 0
while(water>=0):
    water = eval(input('请输入水量：（以负数结束）'))
    if water>0 and water <=220:
        sumWater = sumWater + water * 3.45
    elif water>220 and water<=300:
        sumWater = sumWater + water * 4.83
    elif water>300:
        sumWater = sumWater + water * 5.83
print('总水费为:{}'.format(sumWater))