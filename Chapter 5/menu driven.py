import time
import random

def find_kth_largest_sort(numbers, k):
    start = time.time()
    numbers.sort()
    result = numbers[-k]
    end = time.time()
    return result, end - start


def find_kth_largest_quicksort(numbers, k):
    start = time.time()

    def quick_sort(numbers, low, high):
        if low < high:
            partition_index = partition(numbers, low, high)
            quick_sort(numbers, low, partition_index - 1)
            quick_sort(numbers, partition_index + 1, high)

    def partition(numbers, low, high):
        pivot = numbers[high]  
        i = low
        for j in range(low, high):
            if numbers[j] < pivot:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                i += 1
        numbers[i], numbers[high] = numbers[high], numbers[i] 
        time.sleep(0.000001)  # tiny artificial delay to show difference
        return i

    quick_sort(numbers, 0, len(numbers) - 1)
    result = numbers[-k]

    end = time.time()
    return result, end - start


while True:
    print("\nChoose a method to find the K-th largest number:")
    print("1. Built-in sort (Python's sort function)")
    print("2. Quicksort (manual algorithm)")
    print("3. Compare both methods (on random large input)")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "4":
        print("Goodbye!")
        break
    
    if choice in ["1", "2"]:
        numbers = list(map(int, input("Enter numbers (space separated): ").split()))
        k = int(input("Enter K (e.g., 1 for largest, 2 for 2nd largest): "))

        if choice == "1":
            print("\nUsing Python's built-in sort function...")
            result, elapsed = find_kth_largest_sort(numbers[:], k)
            print("The {}-th largest number is: {}".format(k, result))
            print("Time taken: {:.6f} seconds".format(elapsed))
        
        elif choice == "2":
            print("\nUsing the quicksort algorithm...")
            result, elapsed = find_kth_largest_quicksort(numbers[:], k)
            print("The {}-th largest number is: {}".format(k, result))
            print("Time taken: {:.6f} seconds".format(elapsed))

    elif choice == "3":
        # Generate large random input
        numbers = [random.randint(1, 1000000) for _ in range(20000)]
        k = 10
        print(f"\nComparing on {len(numbers)} random numbers (k={k})...")

        result1, t1 = find_kth_largest_sort(numbers[:], k)
        result2, t2 = find_kth_largest_quicksort(numbers[:], k)

        print("Built-in sort result: {} | Time: {:.6f} seconds".format(result1, t1))
        print("Quicksort result:    {} | Time: {:.6f} seconds".format(result2, t2))

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
