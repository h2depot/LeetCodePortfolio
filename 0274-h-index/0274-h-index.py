class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h = 0
        for i in range(len(citations)+1):
            cnt = 0
            for j in citations:
                if j >= i:
                    cnt += 1
            if cnt >= i:
                h = i
        return h

        