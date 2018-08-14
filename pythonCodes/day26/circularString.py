# code nation program of circular substring
#input given target and source strings
# output is the length of target string to be completed in source

# ex--      ka in "hackerrank"  then "kerra" has length = 5


target = "ka"
source ="hackerrank"
revsource = source[::-1]   # getting reverse of string to check for last   
flag = 0
j,x,count=0,0,0
# following loop checks wether the substring exists in the given string or not
for i in range(len(target)):
    br=1
    for j in range(x,len(source)):
        if(source[j] == target[i]):
            count+=1
            x =j+1
            br=1
            break
        else:
            br = 0
    
    if(br==0):
        print("BREAK",i)
        break    

fval =0
lval = 0
# if count = len of target means substring exists
if(count==len(target)):
    # getting position of first element
    if target[0] in source[0:len(source)-1]:
        fval= source.index(target[0])
    # getting position of last element
    if target[len(target)-1] in revsource[0:len(revsource)-1]:
        lval = revsource.index(target[len(target)-1])
    # printing difference
    print(-fval - lval + len(source)) 
else:
    print("GIVEN TARGET STRING IS NOT A SUBSTRING")
                

