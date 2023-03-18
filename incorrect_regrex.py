import re
N = int(input())
for i in range(N):
    try:
        patt = re.compile(input())
        print("True")
    except:
        print("False")
