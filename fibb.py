#fibonacci
def fib(n):
    if n<0:
        print("invalid")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(9))

#factorial
def fact(n):
    factorial=1
    if n<0:
        print("error")
    elif n==0:
        print("1")
    else:
        for i in range(1,n+1):
            factorial=factorial*i
        print(factorial)
fact(5)




