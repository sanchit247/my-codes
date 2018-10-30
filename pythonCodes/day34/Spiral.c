/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    int a[4][4]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    int i,j,ix=0,iy=0,mx=3,my=3,count=0;
    while(1)
    {
        for(i=iy;i<=my;i++)
        {
            printf("%d ",a[ix][i]);
            count++;            
        }
        ix++;
        if(count==16)
            break;
        for(i=ix;i<=mx;i++)
        {
            printf("%d ",a[i][my]);
            count++;
        }
        my--;
        if(count==16)
            break;
        for(i=my;i>=iy;i--)
        {
            printf("%d ",a[mx][i]);
            count++;
        }
        mx--;
        if(count==16)
            break;
        for(i=mx;i>=ix;i--)
        {
            printf("%d ",a[i][iy]);
            count++;
        }
        iy++;
        if(count==16)
            break;
    }
    

    return 0;
}
