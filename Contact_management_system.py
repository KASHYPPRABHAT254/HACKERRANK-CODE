#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>
char fname[20];
char lname[20];
char pnumber[10];
void acontact();
void vcontact();
void help();
int main()
{
    int x;
    printf("\n\n<--------Welcome To PK Contact Management System------------>\n\n");
    printf("\n[1] Add Contact\n");
    printf("\n[2] View Contact\n");
    printf("\n[3] Help \n");
    printf("\n[4] Exit\n");
    printf("\nPlease Enter One Of The Above Option\n");
    scanf("%d",&x);
    switch(x)
    {
        case 1:
          acontact();
          break;
        
        case 2:
            vcontact();
            break;
        
        case 3:
            help();
            break;
        
        case 4:
          exit(1);
        
        default:
            printf("Please Choose The Correct Option");
            main();
    }
}
    void acontact()
    {
        system("cls");
        printf("\t Enter First Name: ");
        scanf("%s",fname);
        printf("\t Enter Last Name: ");
        scanf("%s",lname);
        printf("\t Enter Phone Number: ");
        scanf("%s",pnumber);
        if(strlen(pnumber)==10)
        {
            FILE *pt;
            pt=fopen("contact.txt","w");
            fputs(fname,pt);
            fputs(lname,pt);
            fputs(pnumber,pt);
            printf("\nContact Added Successfully:");
            fclose(pt);
            main();
            
            
        }
        else
        {
            printf("\n Enter 10 Digit Phone Number Only\n");
            main();
        }
    }
    void vcontact()
    {
        system("cls");
        char rfname[20];
        char rlname[20];
        char rpnumber[15];
        FILE *pt;
        pt=fopen("contact.txt","r");
        fgets(fname,9,pt);
        fgets(lname,10,pt);
        fgets(rpnumber,11,pt);
        printf("\n----------------contact list-----------");
        printf("\nFirst_Name\n",rfname);
        printf("\nLast_Name\n",rlname);
        printf("\nPhone_Number :\n %s",rpnumber);
        main();
    }
    void help()
    {
        printf("\nThis Is A PK management System Aplication");
        main();
    }
