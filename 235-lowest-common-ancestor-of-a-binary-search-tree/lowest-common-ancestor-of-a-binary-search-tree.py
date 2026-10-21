# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            if p.val>node.val:
                if q.val>node.val:
                    return(lca(node.right))
            if p.val<node.val:
                if q.val<node.val:
                   return(lca(node.left))
            return node      
        return lca(root)


        # agar p and q node se chote hain to left side jao 
        # agar p and q dono node se bde hain to right side jao 
        # agar ye dono condition fail hoti hi to node ko return kr do 


        #recursion call me return use krna hai taki answer bhi call ho isliye return lca(node.left) and return lca(node.right)
            
                
            
        