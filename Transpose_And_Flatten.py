import numpy as np
N,M = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
arr = np.array(A)
print(np.transpose(arr))
print(arr.flatten())
    
