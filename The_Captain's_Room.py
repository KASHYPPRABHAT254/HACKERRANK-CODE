# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
n = int(input())
A = map(int,input().split())
C = list(A)
B = set(C)
frequency = collections.Counter(C)
for i in B:
    if(frequency[i]==1):
        print(i)
