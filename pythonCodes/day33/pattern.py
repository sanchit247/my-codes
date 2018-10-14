***
program for n= 5 to print pattern like

     #@@@@@
    ###
   #####
    ###
@@@@@#

***

n=5
m=n
x=1
for i in range(n//2+1):
    print(" "*m,end='')  #same as using for loop
    print("x"*x,end='')
    if(i==0):print("@"*n,end='')
    m-=1
    x+=2
    print("")
m+=1
x-=2
for i in range(n//2):
    if(i==n//2-1):print("@"*n,end="")
    else:print(" "*m,end='')
    x-=2
    print("x"*x,end='')
    print("")
    
        
