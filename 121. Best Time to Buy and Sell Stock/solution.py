# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_value = 0, float('inf')

        for price in prices:
            min_value = min(min_value, price)
            max_profit = max(max_profit, price - min_value)

        return max_profit
