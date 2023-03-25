# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
e  = {}
f = {}
for i in range(N):
    c = input()
    a = ''
    b = []
    for i in c.split():
        if(i.isdigit()):
            b.append(i)
        else:
            a = a+' '+i
    if a in e:
        e[a] = e[a]+1
    else:
        e[a] = 1
print(len(e))
for i in e:
    print(int(e[i]),end=' ')
