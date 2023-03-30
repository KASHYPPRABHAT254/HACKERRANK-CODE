# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
C = []
for i in range(T):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    if(A.issubset(B)):
        C.append("True")
    else:
        C.append("False")
for i in C:
    print(i)
        
