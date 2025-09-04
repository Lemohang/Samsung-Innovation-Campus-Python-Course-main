
def find_kth_largest_sort(numbers, k):
    numbers.sort()
    return numbers[-k]


def find_kth_largest_quicksort(numbers, k):
    def quick_sort(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)

            print("Pivot placed at index {}: {}".format(partition_index, numbers))
            print("Left side: {}".format(numbers[low:partition_index]))
            print("Right side: {}".format(numbers[partition_index+1:high+1]))
            print("-" * 50)

        
            quick_sort(numbers, low, partition_index - 1)
            quick_sort(numbers, partition_index + 1, high)

    def partition(numbers, low, high):
        pivot = numbers[high]  
        print("\nChoosing pivot: {}".format(pivot))
        i = low
        for j in range(low, high):
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
        numbers[i], numbers[high] = numbers[high], numbers[i] 
        return i

    quick_sort(numbers, 0, len(numbers) - 1)
    return numbers[-k]

while True:
    print("\nChoose a method to find the K-th largest number:")
    print("1. Built-in sort (Python's sort function)")
    print("2. Quicksort (manual algorithm with steps)")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "3":
        print("Goodbye!")
        break
    
    numbers = list(map(int, input("Enter numbers (space separated): ").split()))
    k = int(input("Enter K (e.g., 1 for largest, 2 for 2nd largest): "))

    if choice == "1":
        print("\nUsing Python's built-in sort function...")
        result = find_kth_largest_sort(numbers, k)
        print("The {}-th largest number is: {}".format(k, result))
    
    elif choice == "2":
        print("\nUsing the quicksort algorithm(partitioning method)...")
        result = find_kth_largest_quicksort(numbers, k)
        print("\nFinal sorted list: {}".format(numbers))
        print("The {}-th largest number is: {}".format(k, result))
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
