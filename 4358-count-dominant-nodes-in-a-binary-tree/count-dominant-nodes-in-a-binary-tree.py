# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count=0
        def postorder(node):
            nonlocal count
            if not node:
                return float("-inf")
            left=postorder(node.left)
            right=postorder(node.right)
            mx=max(node.val,left,right)
            if mx==node.val:
                count+=1
            return mx
        postorder(root)
        return count


# # mx=Current node ke poore subtree ki maximum value


            
            

        