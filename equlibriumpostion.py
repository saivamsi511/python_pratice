n = int(input())
arr =list(map(int,input().split()))
eq =0
for i in range(1,n-1):
    if sum(arr[:i]) == sum(arr[i+1:]):
        eq = i+1
        break
    elif eq == 0:
        print("not found")
    else:
        print(eq)