#include <stdio.h>

int main()
{
    char *s1,*s2,*temp;
    s1="hello";
    s2 = "world";
    temp = s1;
    s1=s2;
    s2=temp;
    printf("%s %s",s1,s2);

    return 0;
}
