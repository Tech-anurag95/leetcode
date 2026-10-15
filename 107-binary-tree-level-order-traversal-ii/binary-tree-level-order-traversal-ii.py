# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            a=[]
            size=len(queue)
            for i in range(size):
               node=queue.popleft()
               a.append(node.val)
               if node.left:
                    queue.append(node.left)
               if node.right:
                   queue.append(node.right)
            ans.append(a)
        return (ans[::-1])

        
        