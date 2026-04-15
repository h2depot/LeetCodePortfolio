# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        array = []
        def inorder(root, array):
            if root == None:
                return
  
            inorder(root.left, array)
            array.append(root.val)
            inorder(root.right, array)
        inorder(root, array)
        print(array)
        min = float('inf')
        for i in range(len(array)-1):
            min = min if min < array[i+1]-array[i] else array[i+1]-array[i]
        return min