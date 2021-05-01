class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common = ""
        base = strs[0]
        for i, elem in enumerate(base):
            for j in range(1, len(strs)):
                if len(strs[j]) < i + 1 or strs[j][i] != elem:
                    return common
            common += elem
        return common

sol = Solution()
strs = ["flower","flow","flight"]
print(sol.longestCommonPrefix(strs))

