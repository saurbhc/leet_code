# Link: https://leetcode.com/problems/missing-number/

# Time Complexity: O(n)
# Space Complexity: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(0, len(nums)+1):
            if i not in nums:
                return i
