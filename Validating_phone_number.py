# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
N = int(input())
a = []
for i in range(N):
    st = input()
    if(re.findall(r'^[789]\d{9}$',st)):
        a.append("YES")
    else:
        a.append("NO")
for i in a:
    print(i)
