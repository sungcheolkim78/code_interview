from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                max_price = prices[i]

        print(min_price, max_price, max_profit)

        return max_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1, 2, 3, 4, 5]))
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([9, 11, 8, 5, 7, 10]))
