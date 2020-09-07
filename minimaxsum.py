#!/usr/bin/python3
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum +=arr[i]
    return sum

if __name__ == '__main__':
    arr = [1,2,3,4,10,11]
    # arr = list(map(int, input().rstrip().split()))
    print(miniMaxSum(arr))