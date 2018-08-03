import time as t
import random
# a=[1,0,1,1,1,0,0,1,0]
size = 10
#random.randint(1,1000)
a=[]
for i in range(size):
    a.append(random.randint(0,1000))
t1 = t.time()
for i in range(len(a)):
    for j in range(i):
        if(a[i]<a[j]):
            # no need of using temp
            a[i],a[j] = a[j],a[i]
t2 = t.time()
print(t2-t1)
print(size)
print(a)
