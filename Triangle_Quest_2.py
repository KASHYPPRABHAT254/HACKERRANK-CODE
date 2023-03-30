for i in range(1,int(input())+1):
    print((10**i//9)**2)
    
#Below code working far from the constraint provided by the Given problem at hackerrank.
#But Below code does not accepted by the hacker rank so use above uncommented code ---- PRABHAT KASHYAP.
# for i in range(1,int(input())+1):
#     x = lambda a: print(*list(map(int,range(1,a+1))),*list(map(int,range(a-1,0,-1))),sep='')
#     x(i)
