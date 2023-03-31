def max_subarray_sum(arr):
    # Base case
    if len(arr) == 1:
        return arr[0]
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively find the maximum subarray sum for the left half and right half
    max_left = max_subarray_sum(left_half)
    max_right = max_subarray_sum(right_half)
    
    # Find the maximum subarray sum that crosses the midpoint
    print(arr[mid])
    max_cross = max_crossing_sum(arr, mid)
    
    # Return the maximum of the three subarray sums
    return max(max_left, max_right, max_cross)

def max_crossing_sum(arr, mid):
    # Find the maximum subarray sum that crosses the midpoint
    left_sum = float('-inf')
    curr_sum = 0
    for i in range(mid - 1, -1, -1):
        curr_sum += arr[i]
        left_sum = max(left_sum, curr_sum)
        
    right_sum = float('-inf')
    curr_sum = 0
    for i in range(mid, len(arr)):
        curr_sum += arr[i]
        right_sum = max(right_sum, curr_sum)
        
    return left_sum + right_sum

print(max_subarray_sum([0,3,7,-10,4,4,-5,9]))
