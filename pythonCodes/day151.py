# python program to find frequeny of words in a string
s= input("enter the string\n")
a=sorted(s)  #sorted the string
c = ''.join(a)   # a is sorted array so convert it to string
count=1
for i in range(len(c)-1):   # count the frequenc until the next element is different
    if(c[i]==c[i+1]):
        count+=1
        if(i+1==len(c)-1):
            print(c[i],'--',count)
    else:
        print(c[i],'--',count)
        count=1
    if(i==len(c)-2 and c[i]!=c[i+1]):       
        # it it iterated iff the last element of sorted string is different from second last
        print(c[i+1],"--",1)