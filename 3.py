class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s != '':
            start = 0
            end = 0
            sub = s[0]
            max = 1

            while end < len(s)-1:
                start, end, sub, max = self.update(start, end, sub, max, s)

            return max
        else:
            return 0

    def update(self, start, end, sub, max, s):
        newcome = s[end + 1]
        if newcome in sub:
            start = start + sub.index(newcome) + 1
            end = end + 1
            sub = s[start: end + 1]
        else:
            sub += newcome
            end += 1
            if len(sub) > max:
                max = len(sub)

        return start, end, sub, max



s = Solution()
s.lengthOfLongestSubstring('bbbbb')