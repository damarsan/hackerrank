#!/usr/bin/python3

import sys,math

class Calculator():
    def power(self,a,b):
        if (a<0 or b<0):
            raise Exception("n and p should be non-negative")
        return a**b


S = "1"
try :
    string_result = int(S)
    print(string_result)
except:
    print("Bad String")

    
n=-1
p=2
myCalculator=Calculator()
try:
    ans=myCalculator.power(n,p)
    print(ans)
except Exception as e:
        print(e)   