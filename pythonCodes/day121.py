n = int(input("enter the number\n"))
a=[]
def bin(x):
    while(x>=1):
        a.append(int(x%2))
        x= x/2
    return
if(n<0):  #for negative numbers
    m = 0-n #say(n = -5)
    bin(m)    # calculate binary of that number in positive( say 101)
    m=2**len(a)  # gives the maximum equivalent that can be formm with calculated binary equivalent of that number(say 2^3 = 8) 
    m = m+n  #actually it is a subtraction (8 - 5=3)
    a.clear()
    bin(m) # now binary of +3 = binary of -5
else:
    bin(n)     
print("equivalent binary is :\n ")
for i in range(len(a)-1,-1,-1):
    print(a[i])