# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
N = int(input())
for i in range(N):
    a = list(map(str,input().split()))
    if(a[0]=='append'):
        d.append(a[1])
    elif(a[0]=='appendleft'):
        d.appendleft(a[1])
    elif(a[0]=='clear'):
        d.clear()
    elif(a[0]=='extend'):
        d.extend(a[1])
    elif(a[0]=='extendleft'):
        d.extendleft(a[1])
    elif(a[0]=='count'):
        d.count(a[1])
    elif(a[0]=='pop'):
        d.pop()
    elif(a[0]=='popleft'):
        d.popleft()
    elif(a[0]=='remove'):
        d.remove(a[1])
    elif(a[0]=='reverse'):
        d.reverse([1])
    elif(a[0]=='rotate'):
        d.rotate(a[1])
for i in d:
    print(i,end=' ')
