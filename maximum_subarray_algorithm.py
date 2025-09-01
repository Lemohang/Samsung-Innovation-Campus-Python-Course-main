"""
Maximum Subarray Sum Algorithm (Kadane's Algorithm)

This algorithm finds the contiguous subarray with the largest sum in an array of integers.

Approach:
- Uses dynamic programming with memoization
- At each position, decides whether to extend the previous subarray or start a new one
- Tracks both the maximum sum ending at each position and the overall maximum

Time Complexity: O(n)
Space Complexity: O(n)
"""

def max_subarray_sum(arr):
    """
    Find the maximum sum of a contiguous subarray using Kadane's algorithm.
    
    Args:
        arr (list): List of integers
        
    Returns:
        tuple: (max_sum, subarray) where max_sum is the maximum sum and 
               subarray is the actual subarray with maximum sum
    """
    if not arr:
        return 0, []
    
    n = len(arr)
    
    # memo[i] stores the maximum sum ending at index i
    memo = [0] * n
    
    # start[i] stores the starting index of the subarray ending at index i
    start_indices = [0] * n
    
    # Initialize base case
    memo[0] = arr[0]
    start_indices[0] = 0
    max_sum = arr[0]
    left = right = 0
    
    # Fill the memo and start arrays
    for i in range(1, n):
        # Decide whether to start new subarray or extend previous
        if arr[i] > memo[i-1] + arr[i]:
            # Start a new subarray from current element
            memo[i] = arr[i]
            start_indices[i] = i
        else:
            # Extend the previous subarray
            memo[i] = memo[i-1] + arr[i]
            start_indices[i] = start_indices[i-1]
        
        # Update global maximum
        if memo[i] > max_sum:
            max_sum = memo[i]
            left = start_indices[i]
            right = i
    
    return max_sum, arr[left:right+1]


def max_subarray_sum_optimized(arr):
    """
    Optimized version of Kadane's algorithm with O(1) space complexity.
    
    Args:
        arr (list): List of integers
        
    Returns:
        tuple: (max_sum, subarray) where max_sum is the maximum sum and 
               subarray is the actual subarray with maximum sum
    """
    if not arr:
        return 0, []
    
    max_sum = current_sum = arr[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(arr)):
        # If current element is greater than sum + current element,
        # start a new subarray from current element
        if arr[i] > current_sum + arr[i]:
            current_sum = arr[i]
            temp_start = i
        else:
            current_sum += arr[i]
        
        # Update maximum sum and indices if current sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, arr[start:end+1]


# Example usage
if __name__ == "__main__":
    # Test array
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    n = len(arr)
    
    print("Original array:", arr)
    print()
    
    # Using the original algorithm approach
    print("=== Original Algorithm Approach ===")
    memo = [0] * n       # max sum ending at i
    start = [0] * n      # start index of subarray
    
    memo[0] = arr[0]
    start[0] = 0
    max_sum = arr[0]
    l = r = 0
    
    for i in range(1, n):
        # decide whether to start new subarray or extend previous
        if arr[i] > memo[i-1] + arr[i]:
            memo[i] = arr[i]
            start[i] = i
        else:
            memo[i] = memo[i-1] + arr[i]
            start[i] = start[i-1]
        
        # update global maximum
        if memo[i] > max_sum:
            max_sum = memo[i]
            l = start[i]
            r = i
    
    print("Maximum Sum:", max_sum)
    print("Subarray:", arr[l:r+1])
    print("Memo array (max sum ending at each index):", memo)
    print("Start indices:", start)
    print()
    
    # Using our function implementation
    print("=== Function Implementation ===")
    result_sum, result_subarray = max_subarray_sum(arr)
    print("Maximum Sum:", result_sum)
    print("Subarray:", result_subarray)
    print()
    
    # Using optimized version
    print("=== Optimized Implementation ===")
    opt_sum, opt_subarray = max_subarray_sum_optimized(arr)
    print("Maximum Sum:", opt_sum)
    print("Subarray:", opt_subarray)
    print()
    
    # Additional test cases
    print("=== Additional Test Cases ===")
    test_cases = [
        [-1, -2, -3, -4],           # All negative numbers
        [1, 2, 3, 4, 5],            # All positive numbers
        [5, -3, 2, -1, 4],          # Mixed numbers
        [0, 0, 0, 0],               # All zeros
        [1],                        # Single element
        [-5, -2, -8, -1]           # All negative
    ]
    
    for i, test_arr in enumerate(test_cases):
        result_sum, result_subarray = max_subarray_sum_optimized(test_arr)
        print(f"Test {i+1}: {test_arr}")
        print(f"  Maximum Sum: {result_sum}")
        print(f"  Subarray: {result_subarray}")
        print()
