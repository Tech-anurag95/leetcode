# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        ans1=[]
        if root1:
            queue=deque([root1])
            while queue:
                node=queue.popleft()
                ans1.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        ans2=[]
        if root2:
            queue=deque([root2])
            while queue:
                node=queue.popleft()
                ans2.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        ans1+=ans2
        ans1.sort()
        return ans1
        
        
        
        