def nextpermutation(nums:list[int]) ->None:
    for curr in reversed(range(0,len(nums)-1)):
        if nums[curr] >=nums[curr+1]:
            continue
        next = curr +1
        while next < len(nums) and nums[next] > nums[curr]:
            next +=1
        nums[curr],nums[next-1] = nums[next-1],nums[curr]
        nums[curr+1:] = reversed(nums[curr+1:])
        return nums
        return nums.sort()
    
list = [1,1,5]
print(nextpermutation(list))


