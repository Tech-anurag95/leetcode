# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode | None:
        parent=set()
        child=set()
        for num in descriptions:
            parent.add(num[0])
            child.add(num[1])
        for r1 in parent:
            if r1 not in child:
                root=TreeNode(r1)
        nodes={root.val:root}
        for num in descriptions:
            p=num[0]
            c=num[1]
            direction=num[2]
            if p not in nodes:
                nodes[p]=TreeNode(p)
            if c not in nodes:
                nodes[c]=TreeNode(c)
            if direction==1:
                nodes[p].left=nodes[c]
            else:
                nodes[p].right=nodes[c]
        return root
        


        