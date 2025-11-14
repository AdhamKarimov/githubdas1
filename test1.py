a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a<b<c:
    a*=2
    b*=2
    c*=2
else:
    a=-a
    b=-b
    c=-c
print(a,b,c)
