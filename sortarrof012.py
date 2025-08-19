def sort_arr(arr,n):
    count1=0
    count2 =0
    count3 =0
    for i in range(n):
        if arr[i]==0:
            count1 +=1
        elif arr[i] ==1:
            count2+=1
        else:
            count3+=1
    i=0
    while(count1>0):
        arr[i]=0
        i=i+1
        count1 -=1
    while(count2>0):
        arr[i]=0
        i=i+1
        count2 -=1
    while(count3>0):
        arr[i]=0
        i=i+1
        count3 -=1
    return arr
n=5
arr = list(map(int,input().split()))
print(sort_arr(n,arr))
