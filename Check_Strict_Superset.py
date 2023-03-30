# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
try:
    for i in range(n):
        B = set(input().split())
        if(B.issubset(A)):
            if(len(A-B)==0):
                raise TypeError               
        else:
            raise TypeError
    print("True")
except:
    print("False")
