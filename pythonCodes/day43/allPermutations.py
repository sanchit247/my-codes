str = "abc"
s = set()
for i in range (0, len(str)):
    for j in range(0,len(str)):
        for k in range(0,len(str)):
            # if i!= j != k :      # for allowing repeated elements
            if i != j != k != i :
                n = str[i] + str[j] + str[k]
                s.add(n)
print(s)
print(len(s))
