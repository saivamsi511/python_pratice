def count_pairs_of_given_sum(arr,n,k):
    count = 0
    dic = {}
    for i in range(n):
        diff = k-arr[i]
        if diff in dic:
            count = count + dic[diff]
        if arr[i] in dic:
            dic[arr[i]] +=1
        else:
            dic[arr[i]] = 1
    return count
print(count_pairs_of_given_sum([1,5,7,1],4,6))