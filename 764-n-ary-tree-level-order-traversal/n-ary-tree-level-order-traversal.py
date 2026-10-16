"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root==None:
            return []
        ans=[]
        queue=deque([root])
        while queue:
            size=len(queue)
            a=[]
            for i in range(size):
                node=queue.popleft()
                a.append(node.val)
                for child in node.children:
                    queue.append(child)
            ans.append(a)
        return ans
        