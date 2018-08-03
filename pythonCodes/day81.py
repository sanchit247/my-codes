s = [1,5,6,-3,10,-10]
max= 0
a=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]*s[j]>=max):
            max = s[i]*s[j]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if(s[i]*s[j]==max):
            a.append(s[i])
            a.append(s[j])
print(a)
for i in range(0,int(len(a)/2)):
    print("{",a[i],",",a[i+1],"}")
print("maximum product is : " , max)
