def find_sum(n,arr):
    # if n==1:
    #     return arr[0]
    # if arr[0]>arr[1]:
    #     mini=arr[1]
    #     maxi = arr[0]
    # else:
    #     mini = arr[0]
    #     maxi=arr[1]

    # for i in range(2,n):
    #     if arr[i]>maxi:
    #         maxi=arr[i]
    #     elif arr[i]<mini:
    #         mini = arr[i]
    # return mini+maxi
    return max(arr)+min(arr)
n=int(input())
arr = list(map(int,input().split()))
print(find_sum(n,arr))

# in built function