# Enter your code here. Read input from STDIN. Print output to STDOUT
print("Enter any odd number")
a = int(input())
for i in range(1,a+1):
    j = a-i
    while(j>0):
        print(" ",end='')
        j = j - 1
    for k in range(0,2*i-1):
        print("H",end='')
    print("")
    
    
for j in range(0,a+1):
    print(' '.rjust(int((a+1)/2-1)),end='')
    for i in range(0,a):
        print('H',end='')
    print(' '.rjust(5*a-2*a),end='')
    for i in range(0,a):
        print('H',end='')
    print("")
    
    
for i in range(0,int((a+1)/2)):
    print(' '.rjust(int((a+1)/2-1)),end='')
    for j in range(0,5*a):
        print("H",end='')
    print("")
    
    
for j in range(0,a+1):
    print(' '.rjust(int((a+1)/2-1)),end='')
    for i in range(0,a):
        print('H',end='')
    print(' '.rjust(5*a-2*a),end='')
    for i in range(0,a):
        print('H',end='')
    print("")
    
    
for i in range(1,a+1):
    j = 5*a-2*a+a-1
    l = a
    while(l>0):
        for n in range(0,j+1):
            print(" ",end='')
        j = j + 1
        l = l - 1
        
        for k in range(2*a-1,0,-1):
            print("H",end='')
        a = a - 1
        print("")       
    
    
    
    
