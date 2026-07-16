class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        print(prefix)
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        print(suffix)
        ans = []
        for i, num in enumerate(nums):
            ans.append(prefix[i] * suffix[i])
        return ans
        