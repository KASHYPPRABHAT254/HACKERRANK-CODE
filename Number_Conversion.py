number = int(17)
for i in range(1,number + 1):
        #for decimal no
        print((str(i)).rjust(len(str(bin(number)[2:]))+1),end='')
        print((str(oct(i)[2:])).rjust(len(str(bin(number)[2:]))+1),end='')
        print((str(hex(i)[2:])).rjust(len(str(bin(number)[2:]))+1),end='')
        print((str(bin(i)[2:])).rjust(len(str(bin(number)[2:]))+1),end='')
        print("")
        
