"""

"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if int(num1) == 0 or int(num2) == 0:
            return "0"
        len1 = len(num1)
        len2 = len(num2)
        res = [0] * (len1 + len2 - 1)
        ans = ""

        for i in range(len1):
            for j in range(len2):
                res[len1 + len2 - 2 - i - j] += int(num1[i]) * int(num2[j])

        for k in range(len(res) - 1):
            if res[k] >= 10:
                res[k + 1] += res[k] // 10
                res[k] = res[k] % 10

        for k in range(len(res) - 1, -1, -1):
            ans += str(res[k])

        return ans

sol = Solution()
num1 = "123"
num2 = "456"
print(sol.multiply(num1, num2))