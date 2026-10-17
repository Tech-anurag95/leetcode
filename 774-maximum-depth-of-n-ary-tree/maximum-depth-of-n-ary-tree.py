"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root==None:
            return 0
        queue=deque([root])
        ans=0
        while queue:
            size=len(queue)
            ans+=1
            for i in range(size):
                # count=0
                node=queue.popleft()
                for children in node.children:
                    queue.append(children)
        return ans
        