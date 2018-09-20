/******************************************************************************/
#include <stdio.h>
#include<string.h>
int main()
{
    int i,j,k,count =0,flag=0;
    char s[20] ="aaabaa aa", sub[20] ="aa";
    j=0;
    for(i=0;i<=strlen(s)-strlen(sub);i++)
    {
        for(k=i,j=0;j<strlen(sub);j++,k++)
        {
            flag =0;
            if(sub[j]!=s[k])
            {
                flag =1;
                break;
            }
        }
        if(flag!=1)
            count++;
    }
    printf("%d",count);

    return 0;
}
