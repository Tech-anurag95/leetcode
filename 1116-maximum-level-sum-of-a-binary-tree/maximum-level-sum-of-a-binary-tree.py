from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        level=1
        maxlevel=1
        maxsum=float("-inf")
        queue=deque([root])
        while queue:
            size=len(queue)
            total=0
            for i in range(size):
                node=queue.popleft()
                total+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if total>maxsum:
                maxsum=total
                maxlevel=level
            level+=1
        return maxlevel