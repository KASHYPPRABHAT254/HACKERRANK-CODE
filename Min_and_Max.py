import numpy as np
N,M = map(int,input().split())
a = []
for i in range(N):
    b = list(map(int,input().split()))
    a.append(b)
b = np.min(a,axis=1)
print(np.max(b))
