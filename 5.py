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
            for start in range(0, end + 1):
                if start == end:
                    dp[start][end] = True
                    if length < 1:
                        length = 1
                        ret = s[start]
                elif end == start + 1:
                    if s[start] == s[end]:
                        dp[start][end] = True
                        if length < 2:
                            length = 2
                            ret = s[start: end + 1]
                elif end - start >= 2:
                    dp[start][end] = dp[start + 1][end - 1] and (s[start] == s[end])
                    if dp[start][end] == True and end - start + 1 > length:
                        length = end - start + 1
                        ret = s[start: end + 1]

        return ret





sol = Solution()
string = 'ccc'
print(sol.longestPalindrome(string))