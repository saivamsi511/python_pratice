n=5
arr=[1,-1,2,-3,4]
# j=0
# temp=0
# for i in range(0,n):
#     if arr[i]<0:
#         temp =arr[i]        #temp=-1
#         arr[i]= arr[j]      #
#         arr[j] = temp
#         j=j=+1
# print(arr)
low,high = 0,n-1
while(low<high):
    if arr[low]<0:
        low+=1
    elif arr[high]>0:
        high -=1
    else:
        arr[low],arr[high] = arr[high],arr[low]
print(arr)