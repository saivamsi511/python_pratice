arr1=[1,2,3,4,5]
arr2 =[2,4,6,7]
length1 = len(arr1)
length2 = len(arr2)
arr1.sort()
arr2.sort()
arr3 =arr1 + arr2
arr3.sort()
arr2 = arr3[length2]
print(arr1)
print(arr2)
print(arr3)