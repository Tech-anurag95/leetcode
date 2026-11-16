class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        def search(node,val):
            if node==None:
                return None
            if node.val==val:
                return node
            if node.val<val:
                return search(node.right,val)
            else:
                return search(node.left,val)
        return search(root,val)