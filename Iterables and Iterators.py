from itertools import combinations
n = int(input())
l = list(input().split())
k = int(input())
c = list(combinations(l,k))
d = []
for i in c:
    if 'a' in i:
        d.append(i)
print("%.3f" % (len(d)/len(c)))
