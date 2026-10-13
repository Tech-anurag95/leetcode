# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans=[]
        def dfs(root,path,total): #function declaration
            if root==None:  #function defination starts from heere
                return 
            path.append(root.val) 
            total+=root.val
            if root.left==None and root.right==None: #reached the leaf node
               if total==targetSum:
                 ans.append(path.copy())
            dfs(root.left,path,total)
            dfs(root.right,path,total)
            path.pop()
        dfs(root,[],0) #function call
        return ans

            

        