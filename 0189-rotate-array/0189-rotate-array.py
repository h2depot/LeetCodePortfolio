class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        dict = {}
        length = len(nums)
        for i, num in enumerate(nums):
            dict[(i+k)%length] = num
        for i, num in enumerate(nums):
            nums[i] = dict.get(i)