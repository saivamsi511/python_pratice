def checkprime(num):
    if num<2:
        return 0 
    else:
        x=num//2
        for j in range(2,x+1):
            if num%j==0 :
                return 0
    return 1
for i in range(1,100+1):
    if checkprime(i):
        print(i,end=" ")