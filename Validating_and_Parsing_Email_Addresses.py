import email.utils
import re
a = []
email_condition="^[a-zA-Z][a-zA-Z0-9-._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$"
for i in range(int(input())):
    b = email.utils.parseaddr(input())
    # print(b[1])
    if(re.search(email_condition,b[1])):
        a.append(email.utils.formataddr(b))
 for i in a:
    print(i)
