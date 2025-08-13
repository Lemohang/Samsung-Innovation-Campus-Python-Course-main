def multiway_merge(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = multiway_merge(arr[:mid])
    right = multiway_merge(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


arr1 = list(map(int, input("Enter the first list of numbers (separated by spaces): ").split()))
arr2 = list(map(int, input("Enter the second list of numbers (separated by spaces): ").split()))


sorted_arr1 = multiway_merge(arr1)
sorted_arr2 = multiway_merge(arr2)

merged_sorted = merge(sorted_arr1, sorted_arr2)

print("Merged and sorted list:", merged_sorted)