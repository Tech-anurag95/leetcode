# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''CONSIDER THE FIRST NODE IN EACH LEVEL AS THE LEFTMOST NODE'''
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        if root==None:
            return 
        ans=0
        queue=deque([root])
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==0:
                    ans=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans 
        



'''DO LEVEL ORDER TRAVERSAL AND RETURN THE FIRST VALUE OF LAST LEVEL'''
# class Solution:
#     def findBottomLeftValue(self, root: TreeNode | None) -> int:
#         if root==None:
#             return 
#         ans=[]
#         queue=deque([root])
#         while queue:
#             size=len(queue)
#             a=[]
#             for i in range(size):
#                 node=queue.popleft()
#                 a.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             ans.append(a)
#         return ans[-1][0]
        