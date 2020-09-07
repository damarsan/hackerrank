#!/usr/bin/python3
import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        if root is None:
            return -1
        else:
            lDepth = self.getHeight(root.left)
            rDepth = self.getHeight(root.right)
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1


    def levelOrder(self,root):
         queue = [root] if root else []
         while queue:
            node = queue.pop()
            print(node.data, end=" ")
            if node.left: queue.insert(0,node.left)
            if node.right: queue.insert(0,node.right)

T=6
tree = [3,5,4,7,2,1]
myTree=Solution()
root=None
for i in range(T):
    data=tree[i]
    root=myTree.insert(root,data)
myTree.levelOrder(root)