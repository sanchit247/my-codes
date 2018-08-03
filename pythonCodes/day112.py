n = int(input("enter the number\n"))
a=[]
def bin(x):
    while(x>=1):
        rem = int(x%2)
        a.append(rem)
        x= x/2
    return
bin(n)
print("equivalent binary is :\n ")
for i in range(len(a)-1,-1,-1):
    print(a[i])