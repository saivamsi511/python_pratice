s = input()
d= {}
for char in s:
    if char not in d:
        d[char] =1
    else:
        d[char] +=1
print(len(s)-max(d.values()))