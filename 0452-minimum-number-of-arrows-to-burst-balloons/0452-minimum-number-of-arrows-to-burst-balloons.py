class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
            return 0
        points.sort(key = lambda x: x[1])
        ans = 1
        end_prev = points[0][1]
        for point in points:
            start = point[0]
            end = point[1]
            if end_prev < start:
                ans += 1
                end_prev = end
        return ans


        