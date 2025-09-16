def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """

    for i, j in zip(nums1, nums2):
        if i < j:
            pass

    return ""


def findMedianSortedArraysNonEff(nums1, nums2):
    # Step 1: Merge arrays
    merged = []
    i, j = 0, 0

    # Compare and merge while both arrays have elements
    while i < len(nums1) and j < len(nums2):
        # Compare nums1[i] and nums2[j], add smaller to merged
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements from whichever array isn't finished

    merged += nums1[i:]
    merged += nums2[j:]

    # Step 2: Find median from merged array
    total_len = len(merged)
    if total_len % 2 == 1:
        # Odd length: return middle element
        return merged[int((total_len - 1) / 2)]
    else:
        # Even length: return average of two middle elements
        return (merged[int(total_len / 2 - 1)] + merged[int(total_len / 2)]) / 2


nums1 = [2, 3]
nums2 = [4, 5]
print(findMedianSortedArraysNonEff(nums1, nums2))
