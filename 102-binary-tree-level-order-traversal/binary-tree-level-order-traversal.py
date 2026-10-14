# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root==None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            array=[]
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                array.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(array)
        return ans 
        
            
        