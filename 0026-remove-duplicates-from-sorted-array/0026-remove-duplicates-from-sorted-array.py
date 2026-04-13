class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = {}
        k = 0
        for i, num in enumerate(nums):
            if num not in seen:
                nums[k] = num
                k+=1
            seen[num] = i
        return k

            
        