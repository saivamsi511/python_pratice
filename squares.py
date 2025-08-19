s=input()
res = ""
for digit in s:
    res = res+str(int(digit)**2)
print(int(res))