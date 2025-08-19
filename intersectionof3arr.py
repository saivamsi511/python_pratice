arr1 = [1,3,2,4,5,6]
arr2 = [1,3,2,5,6,7]
arr3 = [1,5,2,3,5,6,72]
arr1=set(arr1)
arr2 = set(arr2)
arr3 = set(arr3)
k = arr1.intersection(arr2)
s = list(k.intersection(arr3))
print(s)