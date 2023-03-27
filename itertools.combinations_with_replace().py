# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
a = list(map(str,input().split()))
d = sorted(list(a[0]))
b = combinations_with_replacement(d,int(a[1]))
for i in b:
    c = ''
    for j in i:
        c += j
    print(c)
