import math 
s = input().split()
a = float(s[0])
b = float(s[1])
c = float(s[2])
if b*b==4*a*c:
    x1 = float((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
    print("x1=x2=%.5f" % x1)
elif b*b>4*a*c:
    x1 = float((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
    x2 = float((-b - math.sqrt(b * b - 4 * a * c)) / (2 * a))
    print("x1=%.5f;x2=%.5f" % (x1,x2)) #
elif b*b<4*a*c:
    real = float(-b / (2 * a))
    virtual  = float(math.sqrt(4 * a * c - b * b) / (2 * a))
    print("x1=%.5f+%.5fi;x2=%.5f-%.5fi" % (real+0.00000,virtual,real+0.00000,virtual))
