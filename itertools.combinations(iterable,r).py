from itertools import combinations
S = input()
S = S.split(' ')
B = list(set(S[0]))
k = int(S[1])
A = []
B = []
for i in S[0]:
    A.append(i.upper())
A.sort()
for l in range(1,k+1):
    B = B + list(combinations(A,l))
C = []
for i in B:
        a = ''
        for j in i:
            a = a + j
        C.append(a)
for i in C:
   print(i)
