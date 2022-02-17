"""
2个解
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # solution1:
        #return len(s.strip().split(" ")[-1])

        # solution2:
        i = len(s) - 1
        while s[i] == " " and i >= 0:
            i -= 1
        j = i
        while s[j] != " " and j >= 0:
            j -= 1
        return i - j


sol = Solution()
s = "Hello World"
print(sol.lengthOfLastWord(s))