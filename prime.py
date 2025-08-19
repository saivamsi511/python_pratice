number=int(input("Enter number:-"))
if number>1:
    for i in range(2,(number//2)+1):
        if(number%i) == 0:
            print("not a prime")
            break
        else:
            print("prime")
    else:
        print("not a prime")
