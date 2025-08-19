#0,1,1,2,3,5,13,21,34
#0+1=1,1+1=2,2+1=3,2+3=5

def fib(num):
    if num<0:
        print("incorrect number")
    elif num==0:
        return 0
    elif num==1 or num==2:
        return 1
    else:
        return fib(num-1) + fib(num-2)
print(fib(9))