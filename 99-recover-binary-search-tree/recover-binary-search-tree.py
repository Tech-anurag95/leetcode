# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode | None) -> None:
        a=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)    
            a.append(root) 
            inorder(root.right) 
        inorder(root)
        first=None
        second=None
        for i in range(len(a)-1):
             if a[i].val>a[i+1].val:
                 if first==None:
                     first=a[i]
                 second=a[i+1] 
        first.val,second.val=second.val,first.val
       
        