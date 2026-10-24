# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if root is None:   #agar root nhi hai to return None
            return None
        # root.left,root.right=root.right,root.left #phla level to invert hogya
        # # self.invertTree(root.left) #move to next level and interchange the left node
        # self.invertTree(root.right) #now interchange the right node
        # self.invertTree(root.left)
        # return root
        

        # '''phle left pe jake interchange kro ya right pe farak nhi pdta'''


        def invert(node):
            if node==None:
                return
            node.left,node.right=node.right,node.left
            invert(node.right)
            invert(node.left)
            return (node)
        return invert(root)