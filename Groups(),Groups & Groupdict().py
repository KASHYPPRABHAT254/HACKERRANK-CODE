# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = input()
b =0
try:
    for i in n:
        if(i.isalnum()):
            if(i+i in n):
                print(i)
                b = 1
                raise TypeError
except:
    pass
if(b!=1):
    print("-1")
            
