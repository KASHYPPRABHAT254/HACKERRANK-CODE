# Enter your code here. Read input from STDIN. Print output to STDOUTx
N = int(input())
a = []
for i in range(N):
    a.append(input())
a = set(a)
print(len(a))
