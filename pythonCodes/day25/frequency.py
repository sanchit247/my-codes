s = "abceedfaxd"
dict = {}
for n in s:
    keys = dict.keys()
    if n in keys:
        dict[n]+=1
    else:
        dict[n] =1
print(dict)
