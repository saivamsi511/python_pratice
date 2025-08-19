def min_chocolates(arr):
    arr.sort()
    min_diff = arr[-1] - arr[0]
    for i in range(len(arr)-4):
        min_diff = min(min_diff,arr[i+1]-arr[i])
    return min_diff
arr = [10,4,12,3,1]
result = min_chocolates(arr)
print(result)

# 8 4 2 1
# 1 0 0 1
# 0 0 1 0
# 0 0 0 0  =11
# 0  1  1  0
# 1    1  1  1

# 101>68 =True
