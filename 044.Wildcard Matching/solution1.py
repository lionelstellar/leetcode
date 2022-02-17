"""
dp,分析见leetcode_44.png图片
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            if p[i - 1] == "*":
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] in ("?", s[i - 1]):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]


sol = Solution()
s = "aab"
p = "c*a*b"

print(sol.isMatch(s, p))
