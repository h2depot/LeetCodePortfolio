# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        p = root.left
        q = root.right

        def isSame(p, q):
            if p == None and q == None:
                return True
            elif p == None or q == None:
                return False
            if p.val != q.val:
                return False
            return isSame(p.left, q.right) and isSame(p.right, q.left)
        return isSame(p, q)
        