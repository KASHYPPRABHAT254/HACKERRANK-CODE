# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
b = int(input())
B = set(map(int,input().split()))
A = A.symmetric_difference(B)
print(len(A))
