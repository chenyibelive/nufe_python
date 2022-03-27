side1=float(input("请输入三角形第—条边:"))
side2=float(input("请输入三角形第二条边:"))
side3=float(input("请输入三角形第三条边:"))
if (side1+side2>side3) and (side2+side3>side1) and (side1+side3>side2):
    print("{}、{}、{}可以构成三角形".format(side1,side2,side3))
else:
    print("{}、{}、{}不可以构成三角形".format(side1,side2,side3))
