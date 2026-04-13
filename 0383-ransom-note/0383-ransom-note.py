class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict = {}
        for i, c in enumerate(magazine):
            if not c in dict:
                dict[c] = 1
            else:
                dict[c] += 1
        print(dict)
        for j, k in enumerate(ransomNote):
            if not k in dict:
                return False
            else: 
                dict[k] -= 1
            
            if dict[k] < 0:
                return False
        return True
        