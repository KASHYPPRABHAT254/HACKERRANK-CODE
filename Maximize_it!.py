import itertools
A = list(map(int,input().split()))
K = A[0]
M = A[1]
a = []
for i in range(K):
    a.append(list(map(int,input().split())))
a = itertools.product(*a)
sum = 0
for i in a:
    s = 0
    for j in i:
        s = (s + j**2)%M
        if(s>sum):
          sum = s
print(sum)
