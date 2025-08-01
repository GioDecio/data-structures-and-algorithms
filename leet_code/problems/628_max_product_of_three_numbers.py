# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
def maximumProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    if len(nums) == 3:
        return nums[0] * nums[1] * nums[2]

    max1 = max2 = max3 = float("-inf")
    min1 = min2 = float("inf")

    for n in nums:
        if n > max1:
            max3 = max2
            max2 = max1
            max1 = n
        elif n > max2:
            max3 = max2
            max2 = n
        elif n > max3:
            max3 = n

        if n < min1:
            min2 = min1
            min1 = n
        elif n < min2:
            min2 = n

    maxp = max1 * max2 * max3
    min2max1 = min1 * min2 * max1

    return max(maxp, min2max1)


nums = [1, 2, 3, 4]
print(maximumProduct(nums))
