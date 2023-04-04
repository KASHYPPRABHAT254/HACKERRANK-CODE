# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
a = list(map(int,input().split()))
b = len(list(filter(lambda x: (str(x) == "".join(reversed(str(x)))), a)))!=0
c = len(list(filter(lambda x:x>0,a)))==len(a)
print(all([c,b]))
