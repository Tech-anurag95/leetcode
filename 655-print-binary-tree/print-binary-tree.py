# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: TreeNode | None) -> list[list[str]]:
        if root==None:
            return []
        queue=deque([root])
        height=0
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            height+=1
        m=height
        n=(2**height)-1
        res=[[""]*n for _ in range(m)]
        queue=deque([(root,0,(n-1)//2)])
        while queue:
            node,r,c=queue.popleft() #initially queue me (root,0,(n-1)//2) hai
            res[r][c]=str(node.val) #ab in values ko res matrix me dal denge 
            if node.left:
                queue.append((node.left,r+1,c-2**(height-r-2))) 
            if node.right:
                queue.append((node.right,r+1,c+2**(height-r-2)))
        return res




            
            
        