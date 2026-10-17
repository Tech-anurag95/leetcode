from collections import deque
class Solution:
    def addOneRow(self,root:Optional[TreeNode],val:int,depth:int)->Optional[TreeNode]:
        if depth==1:
            newroot=TreeNode(val)
            newroot.left=root
            return newroot
        abhi=1
        queue=deque([root])
        while queue:
            size=len(queue)
            if abhi==depth-1:
                for i in range(size):
                    curr=queue.popleft()
                    agla1=curr.left
                    agla2=curr.right
                    curr.left=TreeNode(val)
                    curr.right=TreeNode(val)
                    curr.left.left=agla1
                    curr.right.right=agla2
                break
            for i in range(size):    #if abhi!=depth-1 then move to the next level
                curr=queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            abhi+=1   #increment abhi 
        return root