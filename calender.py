#include<stdio.h>
#include<stdlib.h>
int main()
{
    system("Color 3F");
    int year,month,day,i;
    printf("\n Enter your desired year\n");
    scanf("%d",&year);
    char *months[]={"January","Febuary","March","April","May","June","July","August","September","October","November","December"};
    int days[]={31,28,31,30,31,30,31,31,30,31,30,31};
    if(((year%4==0)&&(year%100))||(year%400))
    {
        days[1]=29;
    }
    for(month=0;month<12;month++)
    {
        printf("\n<----------------------------%s------------------------->\n",months[month]);
        printf("\n  SUN     MON     TUE     WED     THU     FRI     SAT\n");
        for(day=1;day<days[month];day++)
        {
           
            printf("%5d   ",day);
            if(day%7==0)
            {
                printf("\n");
            }
            
        }
    }
    
}
