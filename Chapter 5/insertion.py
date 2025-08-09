def insertion_sort(S):
    n = len(S)
    comparisons = 0
    for i in range(1, n):
        print(S)
        x = S[i]
        j = i - 1
        while j >= 0:
            comparisons += 1  
            if S[j] > x:
                S[j + 1] = S[j]
                j -= 1
            else:
                break
        S[j + 1] = x
        print("During insertion {} and No of comparisons: {}".format(x, comparisons))
    print("Total comparisons:", comparisons)

S = [50, 30, 40, 10, 20]
insertion_sort(S)