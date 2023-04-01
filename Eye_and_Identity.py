import numpy
numpy.set_printoptions(legacy='1.13')
a = list(map(int,input().split()))
N = a[0]
M = a[1]
print( numpy.eye(N,M,k=0))
