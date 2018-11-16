"""
       $ 
     $ $ $
   $ $ $ $ $ 
 $ $ $ $ $ $ $ 
 $           $ 
 $ $       $ $ 
 $ $ $   $ $ $ 
 $ $ $ $ $ $ $ 
 $ $ $   $ $ $ 
 $ $       $ $ 
 $           $ 
 $ $ $ $ $ $ $ 
  $ $ $ $ $ 
    $ $ $ 
      $ 
"""

n=5
m=n
i,j=0,1

for i in range(n):
    print(" "*(m-1),"$"*j,"\n",sep="",end="")
    m-=1
    j+=2;
j-=4
for i in range (n-1):
    print("$"*(i+1)," "*j,"$"*(i+1),"\n",sep="",end="")
    j-=2
print("$"*((2*n) - 1))
j=n-1
m=1
for i in range(n-1):
    print("$"*j," "*m,"$"*j,"\n",sep="",end="")
    j-=1
    m+=2
j=2*n -1
for i in range(n):
    print(" "*i,"$"*j,"\n",sep="",end="")
    j-=2
