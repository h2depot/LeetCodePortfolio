class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        length = len(nums)
        cnt = 0
        idx = 0
        while cnt < len(nums):
            num = nums[cnt]
            if num not in hash:
                hash[num] = 1
            else:
                hash[num] += 1
            if hash[num] >= 3:
                nums.pop(cnt)
            else:
                cnt+=1
        print("eventual nums: " + str(nums))
        return len(nums)
