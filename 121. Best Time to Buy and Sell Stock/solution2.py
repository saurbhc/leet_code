# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                max_profit = max(prices[right] - prices[left], max_profit)
            else:
                left = right

            right += 1

        return max_profit
