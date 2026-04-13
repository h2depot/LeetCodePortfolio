class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = len(matrix)
        dict= {}
        ans = []
        for i in range(len(matrix)):
            ans.append(sum(matrix[i]))
        print(ans)
        return ans