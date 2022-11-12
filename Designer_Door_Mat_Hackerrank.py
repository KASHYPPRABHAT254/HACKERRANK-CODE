# Enter your code here. Read input from STDIN. Print output to STDOUT
input_list = list(map(int,input().split()))
a = input_list[0]
b = input_list[1]
c1 = (b-3)//2
c2 = (b-3)//2
for i in range(0,(a-1)//2):
    for j in range(0,c1):
        print("-",end='')
    for k in range(0,i+1):
        print(".|.",end='')
    for k in range(0,i):
        print(".|.",end='')
    for j in range(0,c2):
        print("-",end='')
    c1 = c1 - 3
    c2 = c2 - 3
    print("")
for i in range(0,(b-7)//2):
    print("-",end='')
print("WELCOME",end='')
for i in range(0,(b-7)//2):
    print("-",end='')
print("")
    
    
for i in range(0,(a-1)//2):
    for j in range(0,3*(i+1)):
        print("-",end='')
    for k in range(0,(b-6*(i+1))//3):
        print(".|.",end='')
    for j in range(0,3*(i+1)):
        print("-",end='')
    print("")
    



    
        

