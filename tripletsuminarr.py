n=5
arr=[1,2,3,4,6]
x=10
arr.sort()
for i in arr:
    l=i+1
    k = n-1
    while(i<k):
        sum =arr[i]+arr[l]+arr[k]
        if sum == x:
            print( True)
        if sum<x:
            l+=1
        else:
            k-=1
print(False)