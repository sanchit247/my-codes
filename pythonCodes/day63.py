a=[3,0,1,0,5,9,0,6,7]
for i in range(len(a)):
    for j in range(i):
        if(a[j]==0):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
