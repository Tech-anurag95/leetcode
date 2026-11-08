# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        a=[]
        def postorder(node):
            if node==None:
                return
            postorder(node.left)
            postorder(node.right)
            a.append(node.val)
        postorder(root)
        return a
        