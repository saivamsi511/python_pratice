n=5
arr = [6,-3,-10,0,2]
max_product = arr[0]
pro = arr[0]
min_product = arr[0]
for i in range(1,n):
    if arr[i]<0:
        max_product,min_product = min_product,max_product
        max_product = max(arr[i],max_product*arr[i])
        main_product = min(arr[i],max_product*arr[i])
        pro = max(pro,max_product)
print(pro)
        
