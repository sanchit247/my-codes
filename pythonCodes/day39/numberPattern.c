
#include <stdio.h>

int main()
{
    int n=5,a=100,b=100,l=1;
    float x = 1.9;
    for(int i =0;i<n;i++)
    {
        printf("%f\n ",x);
        x *=a;
        if(l++%2==0)
            x=x+9;
        else
            x = x+1;
        a*=10;
        x/=b;
        b*=10;
    }

    return 0;
}
