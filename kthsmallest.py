n=int(input())
arr = list(map(int,input().split()))
k=int(input("Enter kth index:-"))
if len(arr) ==1:
    print(arr[0])
arr.sort()
print(arr[k+1])
