def find_pairs(arr,sum):
    for i in range(len(arr) - 1):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == sum:
                print(f"pair found:{arr[i],{arr[j]}}")
                return
    print("pair not found")
arr = [1,4,7,8,3,9]
sum_val = 10
find_pairs(arr,sum_val)

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()