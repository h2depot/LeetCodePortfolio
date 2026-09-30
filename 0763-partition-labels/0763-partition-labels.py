class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last_pos = {}
        res = []
        for i, char in enumerate(s):
            last_pos[char] = i
        start = 0
        end = 0
        for i, char in enumerate(s):
            end = last_pos[char] if last_pos[char] > end else end
            if i == end:
                res.append(end - start + 1)
                start = i+1
        return res

        

        