#selection sort
from random import randint
size =randint(1,100)
a=[]
for i in range (size):
    a.append(randint(1,250))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(a[i]>a[j]):
            a[i],a[j] = a[j],a[i]
            j=i+1
print(a)        