"""
"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        i = len(digits) - 1
        while digits[i] + 1 == 10 and i >= 0:
            digits[i] = 0
            i -= 1
        if i == -1:
            digits[0] = 0
            digits.insert(0, 1)
        else:
            digits[i] += 1

        return digits


sol = Solution()
digits = [9,9,9,9]
print(sol.plusOne(digits))