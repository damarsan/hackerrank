#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head 

    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        if head ==None:
            return None
        elif head.next==None:
            return head
        else:
            start=head
            while(start.next!=None):
                current = start.data
                if current == start.next.data:
                    print(f'repeated {current}')
                    start.next = start.next.next
                else:
                    start=start.next
            return head




T=7
list = [1,1,1,1,1,1,1]
mylist= Solution()
head=None
for i in range(T):
    data=list[i]
    head=mylist.insert(head,data) 
head=mylist.removeDuplicates(head)
mylist.display(head); 