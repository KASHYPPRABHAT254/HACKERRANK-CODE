from collections import Counter
total_shoes_avalable = int(input())
size_of_shoes = input()
size_of_shoes = size_of_shoes.split(' ')
size_available = []
for i in size_of_shoes:
    size_available.append(i)
A = dict(Counter(size_available))
cust_no = int(input())
amount = 0
for i in range(cust_no):
    a = input()
    a = a.split()
    try:
        A[a[0]] = A[a[0]] - 1
        if A[a[0]]>=0:
            amount = amount + int(a[1])
    except:
        amount = amount + 0
print(amount)
    
