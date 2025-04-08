def merge_sort(list):
    '''
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    
    Takes overall O(n log n) time
    '''
    if len(list) <= 1:
        return list   # this is our stopping condition (Base case)
    left_half, right_half = split(list)
    # Recursively sort the left half
    left = merge_sort(left_half)
    # Recursively sort the right half
    right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left, right)


def split(list):
    '''
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    
    Takes overall O(k log n) time
    '''
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    '''
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    
    Runs in overall O(n) time
    '''
    l = []
    i = 0
    j = 0

    # Iterate through both lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1

    while j < len(right):
        l.append(right[j])
        j += 1

    return l
    

numbers = [54, 62, 93, 17, 77, 31, 44, 55, 20]
sorted_list = merge_sort(numbers)

print(sorted_list)