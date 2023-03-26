n = int(input())
a = set(map(int,input().split()))
N = int(input())
for i in range(N):
    b = list(map(str,input().split()))
    if(b[0]=='pop'):
        a.pop()
    elif(b[0]=='remove'):
        try:
            a.remove(int(b[1]))
        except:
            continue
    elif(b[0]=='discard'):
        a.discard(int(b[1]))
s = 0
for i in a:
    s += i
print(s)
