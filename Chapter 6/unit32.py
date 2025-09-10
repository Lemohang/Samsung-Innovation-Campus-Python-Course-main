arr = [-2,1,-3,4,-1,2,1,-5,4]
n = len(arr)

memo = [0]*n       
start = [0]*n    

memo[0] = arr[0]
start[0] = 0
max_sum = arr[0]
l = r = 0

for i in range(1,n):
    if arr[i] > memo[i-1] + arr[i]:
        memo[i] = arr[i]
        start[i] = i
    else:
        memo[i] = memo[i-1] + arr[i]
        start[i] = start[i-1]


    if memo[i] > max_sum:
        max_sum = memo[i]
        l = start[i]
        r = i

print("Maximum Sum:", max_sum)
print("Subarray:", arr[l:r+1])