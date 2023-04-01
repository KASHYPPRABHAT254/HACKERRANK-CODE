import numpy as np
N,M = map(int,input().split())
a = []
for i in range(N):
    b = list(map(int,input().split()))
    a.append(b)
b = np.sum(a,axis=0)
# print(np.sum(a,axis=0))
print(np.prod(b))
