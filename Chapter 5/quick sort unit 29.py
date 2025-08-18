def kth_largest_sort(arr, k):
    arr.sort(reverse=True)  # Sort in descending order
    return arr[k-1]         # kth largest is at index k-1

# Example usage:
arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth largest using sort:", kth_largest_sort(arr, k))