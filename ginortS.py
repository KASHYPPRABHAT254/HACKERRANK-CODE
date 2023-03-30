# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
a = []
b = []
c = []
d = []
for i in s:
    if(i.islower()):
        a.append(i)
    elif(i.isupper()):
        b.append(i)
    elif(int(i)%2==1):
        c.append(i)
    else:
        d.append(i)
a.sort()
b.sort()
c.sort()
d.sort()
print(*a,*b,*c,*d,sep='')
