# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode | None) -> TreeNode | None:
        if root==None:
            return
        def sum(node,total):
            if node==None:
                return total
            total=sum(node.right,total)
            node.val+=total
            total=sum(node.left,node.val)
            return total
        sum(root,0)
        return root
        
        

       
            
        