# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        queue=deque([root])
        ans=[]
        a=1
        while queue:
            size=len(queue)
            current=[]
            for i in range(size):
                node=queue.popleft()
                current.append(node.val)
                if node.left!=None:
                    queue.append(node.left)
                if node.right!=None:
                    queue.append(node.right)
            if a%2==0:
                current.reverse()
            ans.append(current)
            a+=1
        return ans