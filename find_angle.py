import cmath
import math
a = int(input())
b = int(input())
z = b/2-a/2j
p = math.degrees(cmath.phase(z))
if p*10%5==0:
    print(math.ceil(p),"\xb0",sep='')
else:
    p = round(p)
    print(p,"\xb0",sep='')
