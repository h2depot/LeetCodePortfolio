class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            target = -nums[i]
            j = i+1
            k = len(nums)-1
            while(j < k):
                sum = nums[j] + nums[k]
                if sum < target:
                    j+=1
                elif sum > target:
                    k-=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j+=1
                    while j < k and nums[k] == nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
        return ans
        