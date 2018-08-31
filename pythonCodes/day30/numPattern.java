import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    System.out.println("enter no. of rows");
		int n =sc.nextInt();
		int l=n; // copy of n for outter loop
		int x =1;
		int y = n*n +1; // calculating the starting value of second loop for  first loop 
		int z=0;
		
		for(int i=0;i<l;i++)
		{
		    for(int j=1 ;j<=n;j++)
		    {
		        System.out.print(x + " ");
		        x++;
		    }
		    z = y;
		    for(int k=1;k<=n;k++)
		    {
		        System.out.print(z + " ");
		        z++;
		    }
		    y = y-(n-1);  // to calculate starting poing each time for second loop
		    n--;
		    System.out.println();
		}
	}
}
