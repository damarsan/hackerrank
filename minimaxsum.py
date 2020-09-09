#!/usr/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    arr_sum = []
    for i in arr:
        arr.remove(i)
        for j in arr:
            sum +=j
        arr_sum.append(sum)
    return arr_sum

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    # arr = list(map(int, input().rstrip().split()))
    print(miniMaxSum(arr))