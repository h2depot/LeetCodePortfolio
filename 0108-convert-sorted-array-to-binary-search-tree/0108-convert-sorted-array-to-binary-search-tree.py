# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def center(nums):
            mid = len(nums)/2
            if not nums:
                return 
            root = TreeNode(val = nums[mid])
            root.left = center(nums[:mid])
            root.right = center(nums[mid+1:])
            return root
        root = center(nums) 
        print(root)
        return root
            