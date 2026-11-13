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

        