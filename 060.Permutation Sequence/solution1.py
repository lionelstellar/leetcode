"""

"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return str(n)
        fact = 1
        factorial = []
        digits = []

        for i in range(1, n):
            fact = fact * i
            factorial.insert(0, fact)
            digits.append(str(i))
        digits.append(str(n))

        res = ""

        for i in range(n - 1):
            digit = digits[(k - 1) // factorial[i]]
            digits.remove(digit)
            k = k % factorial[i]
            res += digit
        res += digits[0]


        return res

sol = Solution()
n = 3
k = 1
print(sol.getPermutation(n, k))