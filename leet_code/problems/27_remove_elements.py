"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
"""


def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            print(nums)
            k += 1
    return k


inputs = {
    3: [[3, 2, 2, 3], [3, 2]],
    # 1: [[1, 2, 3], [3, 2]],
    # 2: [[0, 1, 2, 2, 3, 0, 4, 2], [0, 1, 4, 0, 3]],
}

for key in inputs:
    print(f"Out: {removeElement(inputs[key][0], key)} - Exp {inputs[key][1]}")
