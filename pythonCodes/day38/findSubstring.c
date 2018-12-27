#include <stdio.h>

int main()
{
    char *str="abute",*sub="bat";
    int i=0,j,k,flag=0;
    while(str[i]!='\0')
    {
        if(str[i]==sub[0])
        {
            j=0;
            k=i;
            while(sub[j]!='\0')
            {
               
                if(sub[j]!=str[k])
                {
                  
                    flag=0;
                    break;
                }
                else
                {
                    flag=1;
                    
                }
                j++;
                k++;
            }
        }
        i++;
    }
    if(flag==1)
        printf("substring found");
    else
        printf(" substring not found");
        
    return 0;
}
