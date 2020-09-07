#!/usr/bin/python3
import sys


n=3
#a = [3,2,1]
a = [5,4,3]
numberOfSwaps = 0

for i in a:
    # Track number of elements swapped during a single array traversal
    for j in range(n-1):
        # Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]):
            a[j + 1], a[j] = a[j], a[j + 1]
            numberOfSwaps+=1
    
    # If no elements were swapped during a traversal, array is sorted
    if (numberOfSwaps == 0): 
        break

print(f'Array is sorted in {numberOfSwaps} swaps.')
print(f'First Element: {a[0]}')
print(f'Last Element: {a[len(a)-1]}')