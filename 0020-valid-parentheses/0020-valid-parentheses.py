class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict = { ")":"(", "}":"{","]":"["}
        for i, char in enumerate(s):
            if char not in dict:
                stack.append(char)
            else:
                if len(stack) == 0 or dict[char] != stack.pop():
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
        