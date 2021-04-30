class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = dict[s[-1]]
        i = 0
        while i < len(s) - 1:
            if dict[s[i]] < dict[s[i + 1]]:
                ret -= dict[s[i]]
            else:
                ret += dict[s[i]]
            i += 1

        return ret

sol = Solution()
s = "MCMXCIV"
print(sol.romanToInt(s))
