# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
a = list(input())
for i,j in groupby(a,key = lambda x:x[0]):
    b = []
    # b = tuple(list(i, len(list(j))))
    b.append(len(list(j)))
    b.append(int(i))
    b = tuple(b)
    print(b,end=" ")
