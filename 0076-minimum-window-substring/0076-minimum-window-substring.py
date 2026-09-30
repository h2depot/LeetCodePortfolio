from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_t = Counter(t)
        start = 0
        end = 0
        length = float("inf")
        idx = 0
        window = Counter(s[0])
        have = 0
        if s[0] in dict_t and window[s[0]] == dict_t[s[0]]:
            have += 1
        while start <= end and end < len(s):
            if have == len(dict_t):
                if length > end - start:
                    length = end - start + 1
                    idx = start
                if s[start] in dict_t and window[s[start]] == dict_t[s[start]]:
                    window[s[start]] -= 1
                    have -= 1
                else:
                    window[s[start]] -= 1
                start += 1
            else:
                end += 1
                if end >= len(s):
                    break
                window[s[end]] += 1
                if s[end] in dict_t and window[s[end]] == dict_t[s[end]]:
                    have += 1
        if length == float("inf"):
            return ""
        print(idx)
        print(length)
        return s[idx: idx+length]