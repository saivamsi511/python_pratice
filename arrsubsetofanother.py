def issubset(arr1,arr2):
    for i in arr2:
        if i in arr1:
            continue
        else:
            return "no"
    return "yes"

arr1 = [1,2,3,4,5]
arr2 =[1,2,3]
print(issubset(arr1,arr2))