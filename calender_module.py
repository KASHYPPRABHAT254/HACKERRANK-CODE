import calendar
a = map(int,input().split())
b = []
for i in a:
    b.append(i)
mm = b[0]
dd = b[1]
yyyy = b[2]
calendar.TextCalendar(firstweekday=6).formatyear(yyyy)
day = calendar.weekday(yyyy,mm,dd)
if day==0:
    print("MONDAY")
elif day==1:
    print("TUESDAY")
elif day== 2:
    print("WEDNESDAY")
elif day==3:
    print("THURSDAY")
elif day==4:
    print("FRIDAY")
elif day==5:
    print("SATURDAY")
else:
    print("SUNDAY")    

