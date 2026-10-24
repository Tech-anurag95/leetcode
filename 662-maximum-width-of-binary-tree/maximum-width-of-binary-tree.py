# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if root==None:
            return
        queue=deque([(root,0)])  
        ans=0 
        while queue:
            size=len(queue)    
            first=queue[0][1]
            last=queue[-1][1]
            ans=max(ans,last-first+1)
            for i in range(size):
                node,index=queue.popleft()
                if node.left:
                    queue.append((node.left,2*index))
                if node.right:
                    queue.append((node.right,2*index+1))
        return ans

        # first=queue[0][1] this is index of first node 
        # last=queue[-1][1] this is index of second node



        # IN A BINARY TREE ANY LEVEL CAN HAVE ATMOST 2*LEVEL SUB-NODES
        #AB LEVEL KI BAAT KR RHE HAIN TO BFS-QUEUE YE HI SAB USE HOGA 

        