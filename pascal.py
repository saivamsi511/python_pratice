n=5
for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(" ",end=" ")
    c=1
    for k in range(1,i+1):
        print(" ",c,end=" ")
        c=c*(i-k)//k
    print()

    #         1 
    #       1   1
    #     1   2   1
    #   1   3   3   1
    # 1   4   6   4   1