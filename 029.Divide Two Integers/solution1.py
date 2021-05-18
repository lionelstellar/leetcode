class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        neg_flag = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            neg_flag = 1

        pos_dividend, pos_divisor = abs(dividend), abs(divisor)

        cur = pos_divisor
        list = []
        while pos_dividend >= cur:
            list.append(cur)
            cur <<= 1

        quotient = 0
        for elem in list[::-1]:
            quotient <<= 1
            if pos_dividend >= elem:
                quotient += 1
                pos_dividend -= elem

        if neg_flag:
            quotient = -quotient

        bound = 1 << 31
        if not -bound <= quotient <= bound - 1:
            return bound - 1

        return quotient






sol = Solution()
print(sol.divide(1, 1))