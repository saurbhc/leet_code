# Link: https://leetcode.com/problems/range-sum-query-immutable/

# Time Complexity: O(2n)
# Space Complexity: O(1)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])
