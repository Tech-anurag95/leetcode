# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        from collections import deque
        chota=float("-inf")
        bda=float("inf")
        if root==None:
            return True
        queue=deque([(root,chota,bda)])
        while queue:
            node,chota,bda=queue.popleft()
            if node.val<=chota or node.val>=bda:
                return False
            if node.left:
                queue.append((node.left,chota,node.val))
            if node.right:
                queue.append((node.right,node.val,bda))
        return True
        
            
'''for each node
left node ki min vaue -inf and max value is node.val
right node ki min value is node.val and max val is inf'''
