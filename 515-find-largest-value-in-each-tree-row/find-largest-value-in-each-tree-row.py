# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if root==None:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            size=len(queue)
            a=float("-inf")
            for i in range(size):
                # a=float("-inf")
                node=queue.popleft()
                a=max(node.val,a)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(a)
        return ans


