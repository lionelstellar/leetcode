class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ret = ["" for _ in range(numRows)]
        cycle = 2 * numRows - 2
        round = len(s) // cycle
        remainder = len(s) % cycle
        if remainder != 0:
            round += 1
            pad = "%" * (cycle - remainder)
            s = s + pad

        for i in range(round):
            for j in range(numRows - 1):
                ret[j] = ret[j] + s[i * cycle + j]
            for j in range(numRows - 1):
                ret[numRows - j - 1] = ret[numRows - j - 1 ] + s[i * cycle + numRows - 1 + j]

        ret_str = "".join(ret).replace("%", "")
        return ret_str





sol=Solution()
s = "PAYPALISHIRING"
numRows = 3
print(sol.convert(s, numRows))