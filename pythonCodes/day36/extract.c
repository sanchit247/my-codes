#include <stdio.h>

int main()
{
    float n = 183.32,x;
    int iValue,digitAfterDecimal=2,divisor=1,dValue,mod;  //integer value(iValue), decimal value(dValue)
    for(int i=0;i<digitAfterDecimal;i++)
        divisor*=10;
    iValue=(int)n;
    dValue = (int)(divisor*n - divisor*iValue);
    
    while(dValue>0)
    {
        mod = dValue%10;
        x = (float)mod/divisor;
        x=floor(x*divisor)/divisor;
        printf("%f\n",x);
        divisor/=10;
        dValue/=10;
    }
    int y=1;
    while(iValue>0)
    {
        mod = iValue%10;
        mod = mod*y;
        
        printf("%d\n",mod);
        divisor/=10;
        y*=10;
        iValue/=10;
        
    }
    
    

    return 0;
}
