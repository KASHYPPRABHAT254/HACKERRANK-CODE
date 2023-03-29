# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
c = []
for i in range(T):
    n = int(input())
    a = list(map(int,input().split()))
    b = max(a[0],a[-1])
    try:
        for i in range(n):
            if(b>=a[0] or b>=a[-1]):
                if(a[0]>=a[-1] and b>=a[0]):
                    b = a.pop(0)
                elif(b>=a[-1]):
                    b = a.pop(-1)
                else:
                    raise TypeError
            else:
                raise TypeError
        c.append("Yes")
    except:
        c.append("No")
for i in c:
    print(i)
