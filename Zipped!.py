# Enter your code here. Read input from STDIN. Print output to STDOUT
N,X = map(int,input().split())
a = []
for i in range(X):
    marks = list(map(float,input().split()))
    a = a + [marks]
for i in zip(*a):
    print(sum(i)/X)
