def sortArray(nums):

    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i,len(nums)):
            if nums[j] > nums[i]:
                min_idx = i
        
        if min_idx!=i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]


    return nums

nums = [2,6,1,3]


print(sortArray(nums))

