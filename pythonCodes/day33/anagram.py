str="binary"
s ="brainzy"
arr=[0]*26
a=[0]*26
flag=0;
for i in str:
    arr[ord(i)-97]+=1
for i in s:
    a[ord(i)-97]+=1
for i in range(26):
    if(arr[i]!=a[i]):
        flag=1;
        print("Not anagram")
        break;
if(flag==0):print("Anagram")
        
