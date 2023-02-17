1. Binary Search (for sorted array): 
<br>&nbsp;&nbsp;&nbsp;&nbsp;Time: O(logn)&nbsp;&nbsp;&nbsp;&nbsp;Space: O(1)
```python
# recursive
def binary_search_recursive(arr, left, right, target):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_recursive(arr, left, mid-1, target)
        else:
            return binary_search_recursive(arr, mid+1, right, target)
    else:
        return -1
# iterative
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid[arr] < target:
            left = mid + 1
        elif mid[arr] > target:
            right = mid - 1
        else:
            return mid
    return -1
    
```
2. 