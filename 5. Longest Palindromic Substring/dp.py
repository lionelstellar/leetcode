class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = 0
        ret = ''
        dp = [[False] * len(s) for _ in range(len(s))]

        for end in range(len(s)):
            for start in range(end + 1):
                if start == end:
                    dp[start][end] = True
                elif end == start + 1:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = dp[start + 1][end - 1] and s[start] == s[end]

                if dp[start][end] and end - start + 1 > length:
                    length = end - start + 1
                    ret = s[start: end + 1]


        return ret





sol = Solution()
string = 'c'
print(sol.longestPalindrome(string))