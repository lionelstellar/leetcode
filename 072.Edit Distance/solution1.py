"""
LCS+逆推路径 + max（up, left）求和，部分test case通过，没有AC
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1)
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lcs_length = dp[m][n]

        def dfs(n, i, j, up, left):
            if n == 0:
                return max(i, j)
            if word1[i - 1] == word2[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
                return max(up, left) + dfs(n - 1, i - 1, j - 1, 0, 0)
            if dp[i][j] == dp[i - 1][j] and dp[i][j] == dp[i][j - 1]:
                # up
                # dfs(n, i - 1, j, up + 1, left)
                # left
                # dfs(n, i, j - 1, up, left + 1)
                return min(dfs(n, i - 1, j, up + 1, left), dfs(n, i, j - 1, up, left + 1))
            elif dp[i][j] == dp[i - 1][j]:
                return dfs(n, i - 1, j, up + 1, left)
            else:
                return dfs(n, i, j - 1, up, left + 1)

        return dfs(lcs_length, m, n, 0, 0)



sol = Solution()
word1 = "horse"
word2 = "ros"

# word1 = "intention"
# word2 = "execution"

word1 = "teacher"
word2 = "botcher"
print(sol.minDistance(word1, word2))