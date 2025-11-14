import math
x=float(input("x="))
fx=0
if x>0:
    fx=2*math.sin(x)
elif x<=0:
    fx=x-6
print(fx)
