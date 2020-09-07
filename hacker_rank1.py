#!/usr/bin/python3


def solution(number):
  res=0
  for i in range(number):
    if ((i % 3 ==0) or (i % 5 == 0)):
        res +=i
  return res

def count_bits(n):
    number_of_ones=0
    bin_number = bin(n)
    string_bin = str(bin_number).lstrip("0b")
    print(f'in binary is {string_bin}')
    for i in string_bin: 
        if i == "1":
            number_of_ones += 1 
    
    return number_of_ones

if __name__ == '__main__':
    #N = int(input())
    N=2
    input_string="Hacker"
    even_string=""
    odd_string=""
    for i in range(len(input_string)):
        if (i % 2 ==0):
            even_string += input_string[i]
        else:
            odd_string += input_string[i]
    print(f'{even_string} {odd_string}')

    n = int(input())
    name_numbers = [input().split() for _ in range(n)]
    phone_book = {k: v for k,v in name_numbers}
    while(1):
        try:
            name = input()
            if name in phone_book:
                print('%s=%s' % (name, phone_book[name]))
            else:
                print("Not found")
        except:
            break

