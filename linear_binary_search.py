#Searching Techniques - Linear Search & Binary Search
#Linear Search - Explanation

#Scan the list from start to end and compare each element with the target.

#Works on unsorted and sorted arrays.

#Time complexity: O(n) (best: O(1) if found at index 0).
#Space complexity: O(1).

#Use when array small or unsorted, or when single pass is fine.


#Linear Search - Code

def linear_search(arr, target):
    """
    Return index of target if found, else -1.
    Linear scan from left to right.
    """
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

# Example
arr = [7, 2, 9, 4, 1]
print("Array:", arr)
print("Find 9 ->", linear_search(arr, 9))  # -> index 2
print("Find 5 ->", linear_search(arr, 5))  # -> -1



#Binary Search - Explanation

#Works only on sorted arrays.
#Repeatedly compare target with middle element and eliminate half the search space.
#Time complexity: O(log n), Space complexity: O(1) for iterative, O(log n) for recursive due to stack.

#Two common variants: iterative and recursive. Returns index of any matching element (for duplicates you can adapt to find first/last occurrence).

#Binary Search (Iterative) - Code 

def binary_search_iterative(arr, target):
    """
    arr must be sorted in ascending order.
    Returns index of target if present, else -1.
    """
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Example
arr = [1, 3, 4, 6, 8, 9, 12]
print("Array:", arr)
print("Find 6 ->", binary_search_iterative(arr, 6))  # -> 3
print("Find 7 ->", binary_search_iterative(arr, 7))  # -> -1



#Binary Search (Recursive) - Code (optional for teaching)
def binary_search_recursive(arr, target, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)

# Example
print("Recursive find 9 ->", binary_search_recursive([1,2,5,9,11], 9))  # -> 3

#Edge Cases
#Empty array -> return -1.

#Binary search requires sorted input; otherwise results are undefined.

#For duplicates, binary search returns an arbitrary matching index; to find first/last occurrence use modified binary search.
