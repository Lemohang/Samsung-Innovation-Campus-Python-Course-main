def bubblesort(s):
  counter = 0
  n = len(s)
  for i in range(n):
        print(s)
        for j in range(n-1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
                counter += 1
                
  print("Total swaps:", counter)
        
s=[50,30,40,10,20]
bubblesort(s)
print(s)