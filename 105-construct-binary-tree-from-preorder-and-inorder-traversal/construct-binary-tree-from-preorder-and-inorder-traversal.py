# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self,preorder:list[int],inorder:list[int])->TreeNode|None:
        def construct(pre,inord):
            if not pre or not inord:
                return None
            root=TreeNode(pre[0])
            i=inord.index(pre[0])
            root.left=construct(pre[1:i+1],inord[:i])
            root.right=construct(pre[i+1:],inord[i+1:])
            return root
        return construct(preorder,inorder)

#preorder ka phla element hmesha root hota hai 
#preorder humein order of root btata hai 
#inorder humein which nodes belong to the left and right subtrees btata hai 
        
        #agar inorder ke root wale index ke left me m element hain to preorder ke 1 se start hoke i+1 tak element left subtree me honge aur i+1 se end tak right subtree me honge 