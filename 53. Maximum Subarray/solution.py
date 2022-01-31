# Link: https://leetcode.com/problems/maximum-subarray/

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, cur_sum = float('-inf'), 0

        for n in nums:
            cur_sum = max(cur_sum + n, n)
            max_sum = max(max_sum, cur_sum)

        return max_sum
