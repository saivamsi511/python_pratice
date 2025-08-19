def hexdectodec(n):
    num = n
    base_val = 0
    base = 1
    temp = num
    A,B,C,D,E,F =10,11,12,13,14,15
    while(temp):
        last_digit = temp%10
        temp = int(temp/10)
        base_val += last_digit * base
        base = base * 16
    return base_val
num = 67
print(hexdectodec(num))