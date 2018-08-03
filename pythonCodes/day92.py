
# insertion sort
from random import randint
size =randint(1,100)
a=[]
for i in range (size):
    a.append(randint(1,150))
i=0

while(i!=len(a)-1):
    if(a[i]>a[i+1]):
        a[i],a[i+1] = a[i+1],a[i]
        i=0
    else:
        i+=1
print(a)