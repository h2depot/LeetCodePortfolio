# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        queue = [root]
        hsize = 0
        if not root:
            return 0
        while len(queue) > 0:
            hsize += len(queue)
            tmp = len(queue)
            for i in range(tmp):
                node = queue.pop(0)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        print(hsize)
        return hsize
                

        
        