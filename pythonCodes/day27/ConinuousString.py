s = "sanchit"
ans = []
for i in range(len(s)):
    for j in range(len(s)+1):
        ans.append(s[i:j])


print(list(filter(None,ans)))
