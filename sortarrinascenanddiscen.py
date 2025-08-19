arr = [1,2,3,4,55,13,24,33]
array = sorted(arr)
print(array)
x= array[int(len(arr)/2):]
array[int(len(array)/2):] = reversed(x)
print(arr)
