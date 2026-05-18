import math
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        while(left < right):
            if height[left] > height[right]:
                max_area = max(max_area, height[right] * (right-left))
                right -= 1
            else:
                max_area = max(max_area, height[left] * (right-left))
                left += 1
        return max_area

        