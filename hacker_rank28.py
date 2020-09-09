#!/usr/bin/python


import math
import os
import random
import re
import sys

firstName_dict ={
                'riya':'riya@gmail.com',
                'julia':'julia@julia.me',
                'julia':'sjulia@gmail.com',
                'samantha': 'samantha@gmail.com',
                'tanya': 'tanya@gmail.com'
}

if __name__ == '__main__':
    list_firstName = []
    for key,value in firstName_dict.items():
        if re.search('@gmail.com',value):
            list_firstName.append(key)

list_firstName.sort()
for i in list_firstName:
    print(i)