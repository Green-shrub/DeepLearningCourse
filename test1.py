import math
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
d = (b**2) - (4*a*c)
if d >= 0:
   print("有两个解：")      
   x1 = (-b-math.sqrt(d))/(2*a)
   x2 = (-b+math.sqrt(d))/(2*a)
   print("x1=",x1,"\t","x2=",x2)
else:
    print("此方程没有解")
