import time

def bin1(n, k):
    """Recursive implementation of binomial coefficient"""
    if k == 0 or n == k:
        return 1
    else:
        return bin1(n - 1, k - 1) + bin1(n - 1, k)

def bin2(n, k):
    """Dynamic programming implementation using 2D array"""
    B = [[0] * (i + 1) for i in range(n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if j == 0 or j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i - 1][j - 1] + B[i - 1][j]
    return B[n][k]

def bin3(n, k):
    """Optimized dynamic programming implementation using 1D array"""
    B = [0] * (n + 1)
    for i in range(n + 1):
        for j in range(i, -1, -1):
            if j == 0 or j == i:
                B[j] = 1
            else:
                B[j] = B[j - 1] + B[j]
    return B[k]

def measure_time(func, n, k):
    """Measure execution time of a function"""
    start = time.time()
    result = func(n, k)
    end = time.time()
    return result, end - start

def display_triangle():
    """Display Pascal's triangle using bin3"""
    print("\nPascal's Triangle (first 10 rows) using bin3:")
    for i in range(10):
        for j in range(i + 1):
            print(bin3(i, j), end=' ')
        print()

def main():
    print("Binomial Coefficient Performance Comparison")
    print("==========================================")
    
    while True:
        print("\nMenu:")
        print("1. Compare performance for specific n and k")
        print("2. Display Pascal's Triangle (first 10 rows)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            try:
                n = int(input("Enter n: "))
                k = int(input("Enter k: "))
                
                if k > n or k < 0 or n < 0:
                    print("Invalid input. Please ensure 0 <= k <= n.")
                    continue
                
                print(f"\nCalculating C({n}, {k}):")
                
                # For larger values, we'll skip the recursive method as it's too slow
                if n <= 20:
                    result1, time1 = measure_time(bin1, n, k)
                    print(f"Recursive (bin1):        C({n}, {k}) = {result1} - Time: {time1:.6f} seconds")
                else:
                    print("Recursive (bin1):        Skipped (too slow for n > 20)")
                
                result2, time2 = measure_time(bin2, n, k)
                print(f"2D DP (bin2):            C({n}, {k}) = {result2} - Time: {time2:.6f} seconds")
                
                result3, time3 = measure_time(bin3, n, k)
                print(f"1D DP Optimized (bin3):  C({n}, {k}) = {result3} - Time: {time3:.6f} seconds")
                
                # Analysis
                if n <= 20:
                    fastest = min(time1, time2, time3)
                    if fastest == time1:
                        print("Fastest method: Recursive (for small n)")
                    elif fastest == time2:
                        print("Fastest method: 2D Dynamic Programming")
                    else:
                        print("Fastest method: 1D Optimized Dynamic Programming")
                else:
                    if time2 < time3:
                        print("Fastest method: 2D Dynamic Programming")
                    else:
                        print("Fastest method: 1D Optimized Dynamic Programming")
                        
            except ValueError:
                print("Please enter valid integers.")
            except Exception as e:
                print(f"An error occurred: {e}")
                
        elif choice == '2':
            display_triangle()
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
