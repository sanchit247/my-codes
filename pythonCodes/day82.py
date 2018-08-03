a=[1,3,5,4,8,10,12,13,1]
def compare(c,d,e):
    if(a[c]>a[d] and a[c]>a[e]):
        return c
    elif(a[d]>a[c] and a[d]>a[e]):
        return d
    else:
        return e
print("array is ",a )       
for i in range(1,int(len(a)/2)+2,2):
    max = compare(i-1,i,i+1) # calculate which array index element is greater
    a[i],a[max] = a[max],a[i] #swap i th element with max index element
if(len(a)%2==0 and a[len(a)-1]<a[len(a)-2]):  # for even length array
    a[len(a)-1],a[len(a)-2] = a[len(a)-2],a[len(a)-1]
if(len(a)%2!=0): #for odd length array
    max = compare(len(a)-3,len(a)-2,len(a)-1)
    a[len(a)-2],a[max] = a[max],a[len(a)-2]
print("shuffled array is ",a)
