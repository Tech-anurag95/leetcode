
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root==None:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if i==size-1:
                    ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans