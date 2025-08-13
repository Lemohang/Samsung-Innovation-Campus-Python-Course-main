def search_insert_position(nums, x):
    left = 0 
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == x:
            return mid
        elif nums[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left 

def main():
    nums = [10, 20, 40, 50, 60, 80, 100, 120, 150, 200, 300, 400, 500]
    x = int(input("Input a number to insert: "))
    pos = search_insert_position(nums, x)
    print("{} should be inserted at index {}".format(x, pos + 1))
    nums.insert(pos, x)
    print(nums)

if __name__ == "__main__":
    main()