#!/usr/bin/python3

import sys

class Solution:
        var_stack = [] #LIFO
        var_queue = [] #FIFO
       
        def pushCharacter(self,c):
            self.var_stack.append(c)

        def popCharacter(self):
            return(self.var_stack.pop())

        def enqueueCharacter(self,c):
            self.var_queue.append(c)

        def dequeueCharacter(self):
            # Return if queue is empty 
            if len(self.var_queue) <= 0: 
                return
            # pop an item from the stack 
            x = self.var_queue[len(self.var_queue) - 1] 
            self.var_queue.pop() 
          
            # if stack become empty 
            # return the popped item 
            if len(self.var_queue) <= 0: 
                return x 
              
            # recursive call 
            item = self.dequeueCharacter() 
          
            # push popped item back to 
            # the stack 
            self.var_queue.append(x) 
          
            # return the result of  
            # deQueue() call 
            return item 




# read the string s
s="yes"
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

  
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    