# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
N = int(input())
for i in range(N):
    B = list(input().split())
    C = set(map(int,input().split()))
    operation = B[0]
    set_element_length = B[1]
    if(operation=='intersection_update'):
        A.intersection_update(C)
    elif(operation=='update'):
        A.update(C)
    elif(operation=='difference_update'):
        A.difference_update(C)
    elif(operation=='symmetric_difference_update'):
        A.symmetric_difference_update(C)
print(sum(A))     
