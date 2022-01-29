# Link: https://leetcode.com/problems/missing-number/

# ... XOR Operation for finding the missing Number
# Time Complexity: O(n)
# ... Taking sum of 1st iter will be O(n) and 2nd iter will be O(n)
# ... therefore, O(2n)
# Space Complexity: O(1)
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)
