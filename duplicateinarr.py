arr=[1,2,2,3,4,5]
arr.sort()
n=len(arr)
for i in range(1,n):
    if arr[i-1] == arr[i]:
        print(arr[i])