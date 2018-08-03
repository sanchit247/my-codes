import random
size = 10
a=[]
for i in range(size):
    a.append(random.randint(0,size+8))
a.sort()
print(a)
for i in range(0,len(a)):
    if(a[i]!=i):
        print("missing element is : ",i)
        break
