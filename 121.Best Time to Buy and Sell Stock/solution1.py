class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = prices[0]
        profit_list = [0]
        for elem in prices:
            min_price = min(elem, min_price)
            profit_list.append(max(profit_list[-1], elem - min_price))

        return profit_list[-1]




prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(sol.maxProfit(prices))