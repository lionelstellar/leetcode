#68 ms	14.2 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            digits = []
            while x >= 10:
                digits.append(x % 10)
                x //= 10
            digits.append(x)


            for i in range(len(digits) // 2):
                if digits[i] != digits[len(digits) - 1 - i]:
                    return False
            return True

s = Solution()
print(s.isPalindrome(101))