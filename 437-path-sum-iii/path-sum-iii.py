# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
#         count=0
#         def traversal(node,start,remaining):
#             nonlocal count
#             if node==None:
#                 return
#             if node.val==remaining:
#                 count+=1
#             traversal(node.left,start,remaining-node.val)
#             traversal(node.right,start,remaining-node.val)
#             traversal(node.left,node.left,targetSum) if node.left else None
#             traversal(node.right,node.right,targetSum) if node.right else None
#         if root:
#             traversal(root,root,targetSum)
#         return count

class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        count=0

        def traversal(node,remaining):
            nonlocal count
            if node==None:
                return
            if node.val==remaining:
                count+=1
            traversal(node.left,remaining-node.val)
            traversal(node.right,remaining-node.val)

        def start(node):
            if node==None:
                return
            traversal(node,targetSum)
            start(node.left)
            start(node.right)

        start(root)
        return count
            

        


            

        