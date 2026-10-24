# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        a=[]
        def inorder(node):
            if node==None:
                return
            inorder(node.left)
            a.append(node.val)
            inorder(node.right)
        inorder(root)
        def build(array):
            if not array:
                 return None
            mid=len(array)//2
            root=TreeNode(array[mid])
            root.left=build(array[:mid])
            root.right=build(array[mid+1:])
            return root
        return build(a)