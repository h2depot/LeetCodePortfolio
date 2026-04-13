class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for i, num in enumerate(nums):
            if num not in hash:
                hash[num] = 1
            else:
                hash[num]+=1
            if hash[num] > len(nums)/2:
                return num
        