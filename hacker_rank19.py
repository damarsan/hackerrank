#!/usr/bin/python3
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        res_list = []
        res=0
        for i in range(n+1):
            if i>0:
                if n%i==0:
                    res_list.append(i)
        for i in res_list:
            res +=i
        return res


n = 6
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)