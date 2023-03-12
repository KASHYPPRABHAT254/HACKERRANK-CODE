from itertools import product
A = input()
B = input()
A = A.split(' ')
B = B.split(' ')
A1 = []
for i in A:
    if i.strip():
        A1.append(int(i))

B1 = []
for i in B:
    if i.strip():
        B1.append(int(i))

A1.sort()
B1.sort()
if len(A1)==0 or len(B1)==0:
    print('')
else:
    for i in list(product(A1,B1)):
        print(i,end=' ')
