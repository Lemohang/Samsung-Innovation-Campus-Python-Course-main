def kth_largest_sort(num, k):
    num.sort()             
    return num[-k]         

def quicksort(num, left, right):
    if left < right:
        pos = partition(num, left, right)
        quicksort(num, left, pos - 1)
        quicksort(num, pos + 1, right)

def partition(num, left, right):
    pivot = num[right]
    i = left
    for j in range(left, right):
        if num[j] < pivot:
            num[i], num[j] = num[j], num[i]
            i += 1
    num[i], num[right] = num[right], num[i]
    return i

def kth_largest_quick_sort(num, k):
    quicksort(num, 0, len(num) - 1)
    return num[-k]        

while True:
    print("\nMenu:")
    print("1. Find kth largest using built-in sort")
    print("2. Find kth largest using partition ()")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2":
        num = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("You entered:", num)
        for i in range(len(num)):
            print("recursive call until the pivot is the kth element", partition(num, 0, len(num) - 1))

    
        k = int(input("Enter k: "))
        if choice == "1":
            print(f"{k}th largest element is: {kth_largest_sort(num, k)}")
        else:
            print(f"{k}th largest element is: {kth_largest_quick_sort(num, k)}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")