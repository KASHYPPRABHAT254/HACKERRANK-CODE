# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    a = input()
    try:
        if(float(a)/1==float(a)):
            if( a.count('.')==1):
                print("True")
            else:
                print("False")
        else:
            raise TypeError
    except:
        print("False")
            
                
