def fact(n):
    fact=1
    if n==1:
        return 1
    for i in range(2,n+1):
        fact = fact * i
    return fact
print(fact(5))
