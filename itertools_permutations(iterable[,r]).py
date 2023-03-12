from itertools import permutations
S = input()
S = S.split(' ')
S1 = list(set(S[0]))
k = int(S[1])
A = []
for i in list(permutations(S[0],k)):
    a = ''
    for j in i:
        a = a + j
    A.append(a)
A.sort()
for i in A:
    print(i)
