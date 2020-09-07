#!/usr/bin/python3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
        if head is None:
            head = Node(data)
            self.head = head
        else:
            node = Node(data)
            self.head.next = node
            self.head = node
        return head

mylist= Solution()
T=[2,3,4,1]
head=None
for i in range(len(T)):
    data=int(T[i])
    head=mylist.insert(head,data)    
mylist.display(head) 	  