class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        n = len(nums)
        i = 0
        while i < n:
            start = nums[i]

            # 連続してる間だけ進める
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1

            end = nums[i]

            # 文字列化
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))

            i += 1

        return res
