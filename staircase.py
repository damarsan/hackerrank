#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    x=' '
    y='#'
    for i in range(n+1):
        if i>0:
            print(f'{x*(n-i)}{y*i}')

if __name__ == '__main__':
    n = 6

    staircase(n)