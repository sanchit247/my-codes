/*
split the string in two string when two adjacent carachters are same

*/

#include <stdio.h>

int main()
{
    int i=0,j=0,k=0;
    char *s="hello",o[10],l[10];
   
    while(s[i]!='\0')
    {
        o[j++]=s[i];
        if(s[i]==s[i+1])
           break;
        i++;
    }
    i++;
    while(s[i]!='\0')
        l[k++]=s[i++];
    o[j]='\0';
    l[k]='\0';
    
    puts(o);
    puts(l);
    
    return 0;
}
