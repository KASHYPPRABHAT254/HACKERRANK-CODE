import numpy as np
N = int(input())
A = []
B = []
for i in range(N):
    b = list(map(int,input().split()))
    A.append(b)
for j in range(N):
    b = list(map(int,input().split()))
    B.append(b)
A = np.array(A)
B = np.array(B)
print(np.dot(A,B))
