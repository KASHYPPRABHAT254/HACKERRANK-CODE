# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = input()
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
l = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c,v,c),s,flags=re.IGNORECASE)
if l==[]:
    print(-1)
else:
    for i in l:
        print(i)
