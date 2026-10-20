# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        output=0
        def traversal(node,number):
            nonlocal output
            if node==None:
                return
            total=number+str(node.val)
            if node.left==None and node.right==None:
                output+=int(total)
                return
            traversal(node.left,total)
            traversal(node.right,total)
        traversal(root,"")
        return output

            


        
        