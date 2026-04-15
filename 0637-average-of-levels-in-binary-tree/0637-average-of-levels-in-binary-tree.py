# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        queue = [root]
        ans = []
        idx = 0
        while len(queue) > 0:
            level_len = len(queue)
            sum = 0
            for i in range(len(queue)):
                node = queue.pop(0)
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(float(sum) / float(level_len))
            idx +=1
        return ans