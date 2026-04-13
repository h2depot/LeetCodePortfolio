class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        for i, c in enumerate(reversed(s)):
            if cnt == 0 and c == " ":
                continue
            elif c == " ":
                return cnt
            else:
                cnt +=1
        return cnt
        