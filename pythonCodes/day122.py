n = int(input("enter the number\n"))
def octal(n):
    i=1
    s=0
    while(n>0):
        rem = n%8
        s= s + (rem*i)
        i*=10
        n= int(n/8)
    return s
print("the equivalent octal is :", octal(n))