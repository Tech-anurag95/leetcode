# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        queue=deque([root])
        ans=[]
        while queue:
            node=queue.popleft()
            ans.append(node)
            if node:
                queue.append(node.left)
                queue.append(node.right)
        if None in ans:
            idx=ans.index(None)
            for i in range(idx,len(ans)):
                if ans[i]!=None:
                    return False
        return True

        