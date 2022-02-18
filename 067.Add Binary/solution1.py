"""
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        a.reverse()
        b = list(b)
        b.reverse()
        length = max(len(a), len(b))
        carry = 0
        i = 0
        res = []
        while i < length:
            sum = carry
            if i < len(a):
                sum += int(a[i])
            if i < len(b):
                sum += int(b[i])
            res.append(str(sum % 2))
            carry = sum // 2
            i += 1
        if carry == 1:
            res.append("1")
        res.reverse()
        return "".join(res)

sol = Solution()
a = "1010"
b = "1011"
print(sol.addBinary(a, b))