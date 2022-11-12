    p1 = "1234",p2,B = 50000,w,x,b
    M = 9193950958,A
    char n1[100],n2[100] = "prabhat kashyap",u[100],y[100] = "yes"
    print("\n\n\n\n############# WELCOME TO PK BANKING SYSTEM #############")
    print("\n\nYou Already Have An Account\n Yes/No = ")
    gets(u)
    if(strcmp(u,y)==0):
        print("\a\nPlease Enter Your Name\n")
        gets(n1)
        print("\aPlease Enter Your 4 Digit Password\n")
        input("%d",&p2)
    if((strcmp(n1,n2)==0)&&(p1==p2)):
        print("you have succesfully login\n")
        print("-----OUR SERVICES-----\n")
        print("1. Check Out Current Balance\n")
        print("2. Cash Withdrawl\n")
        print("3. Find Linked Mobile No.\n")
        print("4. Update Mobile No.\n")
        print("5. Update Aadhar No.\n")
        print("6. Exit\n")
        print("\aPlease Select The Option Which Service You Want\n")
        input("%d",&x)
        switch(x)
        
            case 1:
            print("\aYour Current Balance Is $\n\n")
            print("%d",B)
            print("\n\nEnter Any Key TO Go Main Menu")
            return(0)
            case 2:
            print("\aPlease Enter The  Withdrawl Amount = ")
            w = input("%d")
            print("\aYou Withdraw = %d",w)
            b=B-w;
            if(w<=B)
            {
            print("\n\aNow The Current Balance Is = %d",b)
            }
            else
            {
            print("\n\a\aPlease Enter The Valid Amount")
            }
            return(0)
            case 3:
            print("Your Linked Mobile No. Is = %ld",M)
            return(0)
            case 4:
            print("\aPlease Enter The Updated Mobile No.\n")
            input("%ld",&M)
            print("The Updated Mobile No. Is = %ld",M)
            return(0)
            case 5:
            print("Enter The Updated Aadhar No.\n")
            input("%ld",&A)
            print("Your Updated Aadhar No. Is = %ld",A)
            return(0)
            case 6:
            exit(0)

    elif:
        print("\a\a\aPlease Enter The Valid Name Or Password")
        return(1)
    else:
        print("\aEnter Your Name For New Account\n")
        gets(n2)
        print("\aYour Account Name Is = %s",n2)
        print("\nEnter Your Password\n")
        input("%d",&p1)
        print("\aYour Password Is = %d",p1)
        print("\nNow please Login Again")
        
    return(1)
    
}




