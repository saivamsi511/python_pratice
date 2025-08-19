n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for l in range(i+1):
        print("*",end=" ")
    for m in range(i):
        print("*",end=" ")  
    print()
