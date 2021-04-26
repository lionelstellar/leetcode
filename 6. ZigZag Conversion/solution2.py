#Visit by Row: 56 ms	14.4 MB
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ret = ["" for _ in range(numRows)]
        length = len(s)
        i = 0
        m = 0
        while i < length:
            while m < numRows - 1 and i < length:
                ret[m] += s[i]
                i += 1
                m += 1
            while m > 0 and i < length:
                ret[m] += s[i]
                i += 1
                m -= 1

        return "".join(ret)





sol=Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))