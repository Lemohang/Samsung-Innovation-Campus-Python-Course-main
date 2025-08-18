def multiway_merge(lists):
    if len(lists) == 0:
        return []
    if len(lists) == 1:
        return sorted(lists[0]) 
    mid = len(lists) // 2
    left = multiway_merge(lists[:mid])
    right = multiway_merge(lists[mid:])
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

N = int(input("Enter the number of lists to merge: "))
list_of_nums = []
for i in range(N):
    nums = list(map(int, input("Input a list of numbers separated by spaces: ").split()))
    nums.sort()  
    print(nums)
    list_of_nums.append(nums)
merged_sorted = multiway_merge(list_of_nums)
print("Merged sorted:", set(merged_sorted))