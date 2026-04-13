class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        seen = {}

        for i , num in enumerate(nums):
          diff = target - num
          if diff in seen:
            return [seen[diff], i]
          seen[num] = i

            

        