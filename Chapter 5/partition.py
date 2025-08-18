def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] > pivot:  # For kth largest, use '>' for descending order
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low <= high:
        pi = partition(arr, low, high)
        if pi == k-1:
            return arr[pi]
        elif pi > k-1:
            return quickselect(arr, low, pi-1, k)
        else:
            return quickselect(arr, pi+1, high, k)


arr = [7, 10, 4, 3, 20, 15]
k = 3
print("Kth largest using quickselect:", quickselect(arr, 0, len(arr)-1, k))