def coundistinctarr(arr,n):
    res =1
    for i in range(1,n):
        j=0
        for j in range(i):
            if(arr[i]==arr[j]):
                break
        if (i == j+1):
            res +=1
    return res
arr = [1,2,43,34,3,3,3,3,]
n=len(arr)
print(coundistinctarr(arr,n))
