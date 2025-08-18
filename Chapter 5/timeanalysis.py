import time

# Method 1: Using sort()
def find_kth_largest_sort(nums, k):
    nums.sort()
    return nums[-k]

# Method 2: Using partition (Quickselect)
def find_kth_largest_quickselect(nums, k):
    target_index = len(nums) - k

    def partition(left, right):
        pivot = nums[right]  # Last element as pivot
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[store_index] = nums[store_index], nums[i]
                store_index += 1
        nums[store_index], nums[right] = nums[right], nums[store_index]
        return store_index

    left, right = 0, len(nums) - 1
    while True:
        pivot_index = partition(left, right)
        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

# Menu with timing comparison
while True:
    print("\nMenu:")
    print("1. Compare Sort vs Quickselect for K-th largest")
    print("2. Exit")
    
    choice = input("Enter choice (1-2): ")
    if choice == "2":
        print("Goodbye!")
        break

    nums = list(map(int, input("Enter numbers (space separated): ").split()))
    k = int(input("Enter k: "))

    # Sort method timing
    start = time.time()
    result_sort = find_kth_largest_sort(nums[:], k)
    sort_time = time.time() - start

    # Quickselect timing
    start = time.time()
    result_quick = find_kth_largest_quickselect(nums[:], k)
    quick_time = time.time() - start

    print(f"\nK-th largest (Sort): {result_sort} — Time: {sort_time:.6f} seconds")
    print(f"K-th largest (Quickselect): {result_quick} — Time: {quick_time:.6f} seconds")

    if sort_time < quick_time:
        print("\n Sort was faster this time (for small or nearly sorted lists).")
    else:
        print("\n Quickselect was faster this time (good for large unsorted lists).")
