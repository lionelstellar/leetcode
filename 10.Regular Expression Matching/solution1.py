# from right to left
class Solution:
    from functools import lru_cache
    @lru_cache
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if p[-1] == "*":
            return self.isMatch(s, p[:-2]) or \
                   (s and p[-2] in [".", s[-1]]) and self.isMatch(s[:-1], p)
        else:
            return s and p[-1] in [".", s[-1]] and self.isMatch(s[:-1], p[:-1])

s = "aa"
p = "a"
sol = Solution()
print(sol.isMatch(s, p))


