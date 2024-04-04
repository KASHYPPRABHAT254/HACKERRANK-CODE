n = int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end='')
    for k in range(1,n+1):
        print(k,end='')
    if(k==1):
        break
    n = n-2
    print('')
