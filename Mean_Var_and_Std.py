import numpy as np
N,M = map(int,input().split())
a = []
for i in range(N):
    b = list(map(float,input().split()))
    a.append(b)
arr = np.array(a)
print(np.mean(arr,axis=1))
print(np.var(arr,axis=0))
print((np.std(arr)).round(11))
