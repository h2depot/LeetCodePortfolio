class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        kaibun = ""
        for i, c in enumerate(s):
            if 65 <= ord(c) <= 90:
                kaibun += chr(ord(c) + 32)
            elif 48 <= ord(c) <= 57:
                kaibun += c
            elif not c.isalpha():
                continue
            else:
                kaibun += c
        print(kaibun)
        for i in range(len(kaibun)/2):
            if kaibun[i] != kaibun[-i-1]:
                return False
        return True
        