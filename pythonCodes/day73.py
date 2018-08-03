import random
size = random.randint(1,1000)
a=[]
count = 0
for i in range(size):
    a.append(random.randint(1,700))
print(a)
for i in range(len(a)):
    for j in range(i):
        if(a[i]<a[j]):
            a[i],a[j] = a[j],a[i]
count=0
temp=0
x=0
for i in range(len(a)):
    i=x
    if((i+1)<len(a)):
        while(a[i]==a[i+1]):
            count=i+1   # any value can be here so that count not remain 0
            i+=1
            if(i==len(a)-1):
                break
    if(count!=0 and (a[temp]!=a[i] or temp==0) ):   # temp==0 so thatit can take first element also
        print(a[i]," is duplicated")
        count = 0
        temp=i # so that it does not print for triplet or more
    if(i>=len(a)):
        break
    x=i+1


# or
"""
s = set()
for x in range(len(a)):
    if a[x] in a[x+1:]:
        s.add(a[x])
print(s)

"""
