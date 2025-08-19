k=3
n=5
arr=[3,9,12,16,20]
arr.sort()
smallest = arr[0]+k
largest = arr[n-1]-k
diff = arr[n-1] -arr[0]
for i in range(1,n):
    if arr[i]-k<0:
        continue
    mini = min(smallest,arr[i]-k)
    maxi = max(largest,arr[i-1]+k)
    diff = min(diff,maxi-mini)
print(diff)