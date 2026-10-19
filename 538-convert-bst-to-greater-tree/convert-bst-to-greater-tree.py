# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
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
        