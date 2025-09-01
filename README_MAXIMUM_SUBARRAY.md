# Maximum Subarray Sum Algorithm (Kadane's Algorithm)

## Problem Statement
Given an array of integers (both positive and negative), find the contiguous subarray with the largest sum and return that sum.

## Algorithm Explanation

The provided algorithm implements Kadane's algorithm, which is an efficient dynamic programming solution to the maximum subarray problem.

### Key Concepts

1. **Dynamic Programming Approach**: At each position, we decide whether to:
   - Extend the existing subarray by including the current element
   - Start a new subarray from the current element

2. **State Definition**:
   - `memo[i]`: Maximum sum of subarray ending at index `i`
   - `start[i]`: Starting index of the subarray that gives the maximum sum ending at index `i`

3. **Recurrence Relation**:
   ```
   memo[i] = max(arr[i], memo[i-1] + arr[i])
   ```

### Algorithm Steps

1. **Initialization**:
   - `memo[0] = arr[0]` (first element is the max sum ending at index 0)
   - `start[0] = 0` (subarray starts at index 0)
   - `max_sum = arr[0]` (global maximum)
   - `l = r = 0` (indices of the maximum subarray)

2. **Iteration** (for i from 1 to n-1):
   - If `arr[i] > memo[i-1] + arr[i]`:
     - Start new subarray: `memo[i] = arr[i]`, `start[i] = i`
   - Else:
     - Extend previous subarray: `memo[i] = memo[i-1] + arr[i]`, `start[i] = start[i-1]`
   - If `memo[i] > max_sum`:
     - Update global maximum: `max_sum = memo[i]`, `l = start[i]`, `r = i`

3. **Result**: Maximum sum is `max_sum`, and the subarray is `arr[l:r+1]`

### Example Walkthrough

For array `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`:

| i | arr[i] | memo[i] | start[i] | max_sum | l | r | Subarray       |
|---|--------|---------|----------|---------|---|---|----------------|
| 0 | -2     | -2      | 0        | -2      | 0 | 0 | [-2]           |
| 1 | 1      | 1       | 1        | 1       | 1 | 1 | [1]            |
| 2 | -3     | -2      | 1        | 1       | 1 | 1 | [1]            |
| 3 | 4      | 4       | 3        | 4       | 3 | 3 | [4]            |
| 4 | -1     | 3       | 3        | 4       | 3 | 3 | [4]            |
| 5 | 2      | 5       | 3        | 5       | 3 | 5 | [4, -1, 2]     |
| 6 | 1      | 6       | 3        | 6       | 3 | 6 | [4, -1, 2, 1]  |
| 7 | -5     | 1       | 3        | 6       | 3 | 6 | [4, -1, 2, 1]  |
| 8 | 4      | 5       | 3        | 6       | 3 | 6 | [4, -1, 2, 1]  |

### Time and Space Complexity

- **Time Complexity**: O(n) - Single pass through the array
- **Space Complexity**: O(n) - For the memo and start arrays

### Optimized Version

An optimized version can achieve O(1) space complexity by only keeping track of the current sum and maximum sum, rather than storing all intermediate values.

## Applications

1. **Financial Analysis**: Finding the most profitable period for investments
2. **Signal Processing**: Identifying the strongest signal in a noisy environment
3. **Bioinformatics**: Finding significant subsequences in DNA or protein sequences
4. **Resource Allocation**: Determining optimal allocation periods

## Related Algorithms

- **Maximum Product Subarray**: Similar problem but with multiplication
- **Maximum Sum Subarray with Constraints**: Adding constraints like minimum length
- **2D Maximum Sum Subarray**: Extending to 2D arrays (matrices)
