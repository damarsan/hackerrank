#!/usr/bin/python3

n_number = [3,4,5,7,11,13,17,19,23,29,31,37,41,43,47,48,53,59,61,67,71]
n_number = [1]
n = len(n_number)
if len(n_number) ==1 and n_number[0] ==1:
    print("Not  prime")
else:
    for i in range(n): 
        result="Prime"
        for j in range(2,n_number[i]):
            if n_number[i] % j == 0:
                result="not prime"
                break

        print(n_number[i],result)




for i in range(n):
    n_number=int(input())
    result="Prime"
    if n_number ==1:
        result="Not prime"
    else:
        if(n_number % 2 == 0 and n_number > 2):
            result="Not prime"
        else:
            for j in range(3, int(n_number**(1/2))+1, 2):
                if n_number % j == 0:
                    result="Not prime"
                    break

    print(result)