import numpy
N,M,P = map(int,input().split())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))
B = []
for i in range(M):
    B.append(list(map(int,input().split())))
arr1 = numpy.array(A)
arr2 = numpy.array(B)
print(numpy.concatenate((arr1,arr2),axis=0))
