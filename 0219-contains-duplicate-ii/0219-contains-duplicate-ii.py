class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash = {}
        for i, num in enumerate(nums):
                if num in hash and abs(hash[num] - i) <= k:
                    return True
                hash[num] = i
        return False
        