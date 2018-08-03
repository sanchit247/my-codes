#n = [int(x) for x in input("enter the ").split()]
n=[2,5,7,0,1,3,4,8,9,10]
m=[]
for i in range(len(n)):
    if(i not in n):
        break
    else:
        m.append(i)
# m prints element
l=[]
for i in range(len(m)):
    for j in range(len(n)):
        if(m[i] == n[j]):
           l.append(j) 
# l prints indexes
l.sort()
s=[]
for i in l:
    s.append(n[i])
print(s)
