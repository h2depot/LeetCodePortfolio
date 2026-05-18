class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()

        seq = 1
        max = 0
        print(nums)
        for i in range(0, len(nums) - 1):
            print("for loop !")
            print(nums[i]+1)
            print(nums[i+1])
            if nums[i]+1 == nums[i+1]:
                seq += 1
                print("equal")
            else:
                max = max if max > seq else seq
                seq = 1
                print("not equal")
        max = max if max > seq else seq
        return max
