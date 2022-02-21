"""
dp, 0行列为空字符串
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for k in range(0, n + 1):
            dp[0][k] = k
        for k in range(0, m + 1):
            dp[k][0] = k

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        edit_distance = dp[m][n]
        # print(dp)
        return edit_distance




sol = Solution()
word1 = "horse"
word2 = "ros"

# word1 = "intention"
# word2 = "execution"

word1 = "teacher"
word2 = "botcher"
print(sol.minDistance(word1, word2))