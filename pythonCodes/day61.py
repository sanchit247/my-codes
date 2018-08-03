import random
size = int(input("enter the size of array\n"))
a=[]
for i in range(0,size):
    a.append(random.randint(-10,10))
print(a,"\n")
count = 0
for i in range(1,size):
    for j in range(0,size-i+1):
        sum = 0
        for k in range(j,j+i):
            sum+=a[k]
        if(sum==0):
            print(a[j:j+i])
            count+=1
            
print("there are total ", count , " sub-arrays having sum zero\n")


# another way
"""
l=[int(x) for x in input("enter Numbers Seperated By space").split()]
sum=0
for i in range(len(l)):
     for j in range(i,len(l)):  #creating loop for all posiible subarray from elemnt liyh index
          sum+=l[j]             #calculating the sum
          if(sum==0):           
               print(l[i:j+1])  #if sum equal zero the printing the particular sub array
     sum=0
"""

