def dectobinary(n):
    s = bin(n)[2:]
    print(s)
    loc1 = s[s.index('1'):]
    return loc1
    return "0"
num = 17
print(dectobinary(num))
