
size = int(input())
l = size
for i in range(size-1,-1,-1):
    k1 = l
    k2 = l
    #for upper left ----
    for j in range(0,(l-1)*2):
        print("-",end='')
    #upper left portion 
    if(i!=size-1):
        for j in range(size-1,i,-1):
            print(chr(65+j).lower(),end='')
            print("-",end='')
    print(chr(65+i).lower(),end='')
        
    #upper right portion
    if(i!=size-1):
        for j in range(i+1,size):
            print("-",end='')
            print(chr(65+j).lower(),end='')
                
    #for upper right ------ 
    for j in range(0,(l-1)*2):
        print("-",end='')
    print("")
    l = l - 1
        
        
k3 = 2
k4 = 1
k5 = 1   
for i in range(size-1,0,-1):
    #for lower left -----
    for j in range(0,k3):
        print("-",end='')
    #lower left portion
    if(i!=1):
        for j in range(size-1,k4,-1):
            print(chr(65+j).lower(),end='')
            print("-",end='')
        k4 = k4 + 1
    print(chr(65+k5).lower(),end='')
    k5 = k5 + 1
        
    #lower right portion
    if(i!=1):
        for j in range(size-i+1,size):
            print("-",end='')
            print(chr(65+j).lower(),end='')
    #lower right ---
    for j in range(0,k3):
        print("-",end='')
    k3 = k3 + 2
    print("")
        
        
