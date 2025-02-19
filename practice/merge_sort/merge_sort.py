def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


## WRITE MERGE_SORT FUNCTION HERE ##
def merge_sort(my_list):
    if len(my_list)<=1:
        return my_list
    mid_index = len(my_list)//2
    left= merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])
    combined = merge(left, right)
    return combined





original_list = []

sorted_list = merge_sort(original_list)

print('Original List:', original_list)
print('\nSorted List:', sorted_list)



"""
    EXPECTED OUTPUT:
    ----------------
    Original List: [3, 1, 4, 2]
    
    Sorted List: [1, 2, 3, 4]
    
 """